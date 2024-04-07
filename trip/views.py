import csv
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
from trip.serializer import CasetaSerializer, RutaSerializer, UserSerializer, VehiculoSerializer, ViajeSerializer

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
    serializer_class = ViajeSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    files = {
        ("Mexicali", "Tecate"): "data/mxl-tec.csv",
        ("Mexicali", "Tijuana"): "data/mxl-tij.csv",
        ("Mexicali", "Rosarito"): "data/mxl-ros.csv",
        ("Mexicali", "Ensenada"): "data/mxl-ens.csv",
        ("Tecate", "Mexicali"): "data/mxl-tec.csv",
        ("Tijuana", "Mexicali"): "data/mxl-tij.csv",
        ("Rosarito", "Mexicali"): "data/mxl-ros.csv",
        ("Ensenada", "Mexicali"): "data/mxl-ens.csv",
    }
    
    columns = {
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
    
    @action(detail=False, methods=['post'])
    def generate(self, request):
        destinations = request.data.get('destinations', [])
        passengers = request.data.get('passengers', '')
        vehicle = request.data.get('vehicle', '')
        
        if tuple(destinations[:2]) in self.files and vehicle in self.columns:
            filename = self.files[tuple(destinations[:2])]
            column = self.columns[vehicle]
            
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                
                total_cost = 0
                details = []
                for row in reader:
                    cost = float(row[column]) if row[column] else 0.0
                    
                    if row[0] == "Totales":
                        total_cost += cost
                    else:
                        details.append({
                            "nombre": row[0],
                            "costo": cost,
                            "carretera": row[2],
                            "tiempo": row[4],
                            "caseta": row[5]
                        })
                
                if len(destinations) == 3 and destinations[0] == destinations[2]:
                    total_cost *= 2
                    details += details[::-1]
                
                return Response({
                    "costo_total": total_cost,
                    "detalles": details
                })
        
        return Response({"error": "Destinaciones o vehículo no válidos"})

class RutaViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all().order_by('-id')
    serializer_class = RutaSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class CasetaViewSet(viewsets.ModelViewSet):
    queryset = Stand.objects.all().order_by('-id')
    serializer_class = CasetaSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all().order_by('-id')
    serializer_class = VehiculoSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
