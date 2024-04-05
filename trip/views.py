from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from trip.models import Caseta, Ruta, Vehiculo, Viaje
from trip.serializer import CasetaSerializer, RutaSerializer, VehiculoSerializer, ViajeSerializer

class ViajeViewSet(viewsets.ModelViewSet):
    queryset = Viaje.objects.all().order_by('-id')
    serializer_class = ViajeSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all().order_by('-id')
    serializer_class = RutaSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class CasetaViewSet(viewsets.ModelViewSet):
    queryset = Caseta.objects.all().order_by('-id')
    serializer_class = CasetaSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all().order_by('-id')
    serializer_class = VehiculoSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
