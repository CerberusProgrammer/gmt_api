import csv
from django.utils.dateparse import parse_datetime
from datetime import timedelta

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response

from trip.models import Stand, Route, Vehicle, Trip
from trip.serializer import StandSerializer, RouteSerializer, UserSerializer, VehicleSerializer, TripSerializer

class UserCreate(APIView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ViajeViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all().order_by('-id')
    serializer_class = TripSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    files = {
        ("Mexicali", "Tecate"): "data/mxl-tec.csv",
        ("Mexicali", "Tijuana"): "data/mxl-tij.csv",
        ("Mexicali", "Rosarito"): "data/mxl-ros.csv",
        ("Mexicali", "Ensenada"): "data/mxl-ens.csv",
        ("Tecate", "Mexicali"): "data/tec-mxl.csv",
        ("Tijuana", "Mexicali"): "data/tij-mxl.csv",
        ("Rosarito", "Mexicali"): "data/ros-mxl.csv",
        ("Ensenada", "Mexicali"): "data/ens-mxl.csv",
        ("Tecate", "Tijuana"): "data/tec-tij.csv",
        ("Tecate", "Rosarito"): "data/tec-ros.csv",
        ("Tecate", "Ensenada"): "data/tec-ens.csv",
        ("Tijuana", "Tecate"): "data/tij-tec.csv",
        ("Tijuana", "Rosarito"): "data/tij-ros.csv",
        ("Tijuana", "Ensenada"): "data/tij-ens.csv",
        ("Rosarito", "Tecate"): "data/ros-tec.csv",
        ("Rosarito", "Tijuana"): "data/ros-tij.csv",
        ("Rosarito", "Ensenada"): "data/ros-ens.csv",
        ("Ensenada", "Tecate"): "data/ens-tec.csv",
        ("Ensenada", "Tijuana"): "data/ens-tij.csv",
        ("Ensenada", "Rosarito"): "data/ens-ros.csv",
    }
    
    columns = {
        "Motocicleta": 6,
        "Camión 3 ejes": 7,
        "Camión 4 ejes": 8,
        "Camión 5 ejes": 9,
        "Camión 6 ejes": 10,
        "Camión 7 ejes": 11,
        "Camión 8 ejes": 12,
        "Camión 9 ejes": 13,
        "Automóvil": 14,
        "Automóvil remolque 1 eje": 15,
        "Automóvil remolque 2 eje": 16,
        "Pick Ups": 17,
        "Autobus 2 ejes": 18,
        "Autobus 3 ejes": 19,
        "Autobus 4 ejes": 20,
        "Camión 2 ejes": 21,
    }
    
    salario_minimo = 141.70
    costo_combustible_por_litro = 20
    
    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user).order_by('-id')
    
    @action(detail=False, methods=['post'])
    def generate(self, request):
        destinations = request.data.get('destinations', [])
        passengers = int(request.data.get('passengers', 0))
        vehicle_name = request.data.get('vehicle', '')
        datetime_obj = parse_datetime(request.data.get('datetime', ''))
        viaticos_por_dia = 6 * self.salario_minimo
        
        total_cost = 0
        total_details = []
        total_time = timedelta()
        total_viaticos = 0
        total_kilometraje = 0
        
        vehicle = Vehicle.objects.create(name=vehicle_name, cost=0)
        
        for i in range(len(destinations) - 1):
            if (destinations[i], destinations[i+1]) in self.files and vehicle.name in self.columns:
                filename = self.files[(destinations[i], destinations[i+1])]
                column = self.columns[vehicle.name]
                
                with open(filename, 'r') as file:
                    reader = csv.reader(file)
                    next(reader)
                    
                    details = []
                    for row in reader:
                        if column < len(row):
                            cost = float(row[column]) if row[column] else 0.0
                        else:
                            cost = 0.0
                        
                        if row[0] == "Totales":
                            total_cost += cost
                            total_kilometraje += float(row[3]) if row[3] else 0.0
                        else:
                            stand_name = row[5] if row[5] else None
                            if stand_name:
                                stand = Stand.objects.create(name=stand_name)
                                vehicle.cost = cost
                                vehicle.save()
                                stand.vehicles.add(vehicle)
                            else:
                                stand = None
                            
                            time = row[4].split(':')
                            total_time += timedelta(hours=int(time[0]), minutes=int(time[1]))
                            
                            route = Route.objects.create(
                                name=row[0],
                                state="",
                                road=row[2],
                                length=float(row[3]) if row[3] else 0.0,
                                time=row[4],
                                stand=stand
                            )
                            details.append(route)
                    
                    total_details += details
        
        total_viaticos = total_time.total_seconds() / 3600 * viaticos_por_dia
        total_cost += total_viaticos
        
        costo_combustible = (total_kilometraje / 3) * self.costo_combustible_por_litro
        total_cost += costo_combustible
        
        vehiculos_requeridos = -(-passengers // 4)
        total_cost *= vehiculos_requeridos
        
        to_city_date = datetime_obj + total_time
        
        trip = Trip.objects.create(
            from_city=destinations[0],
            to_city=destinations[1],
            from_city_date=datetime_obj,
            to_city_date=to_city_date,
            travel_cost=round(total_viaticos, 2),
            total_cost=round(total_cost, 2),
            gasoline_cost=round(costo_combustible, 2),
            passengers=passengers,
            user=request.user
        )
        trip.routes.set(total_details)
        
        return Response(TripSerializer(trip).data)
    
class RutaViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all().order_by('-id')
    serializer_class = RouteSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class CasetaViewSet(viewsets.ModelViewSet):
    queryset = Stand.objects.all().order_by('-id')
    serializer_class = StandSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all().order_by('-id')
    serializer_class = VehicleSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
