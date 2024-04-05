from rest_framework import serializers
from django.contrib.auth.models import User

from trip.models import Stand, Route, Vehicle, Trip

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

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