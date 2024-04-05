from rest_framework import serializers

from trip.models import Caseta, Ruta, Vehiculo, Viaje

class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = '__all__'

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'

class CasetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caseta
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'