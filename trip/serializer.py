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

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class StandSerializer(serializers.ModelSerializer):
    vehicles = VehicleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Stand
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    stand = StandSerializer(read_only=True)

    class Meta:
        model = Route
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True, read_only=True)
    
    class Meta:
        model = Trip
        fields = '__all__'