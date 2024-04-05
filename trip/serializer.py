from rest_framework import serializers

from trip.models import Stand, Route, Vehicle, Trip

class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class CasetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stand
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'