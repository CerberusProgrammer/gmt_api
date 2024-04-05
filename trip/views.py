from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


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
