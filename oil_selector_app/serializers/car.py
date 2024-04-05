from rest_framework import serializers
from ..models.car import Car, CarMake, CarModel, CarEngine

class CarEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarEngine
        fields = ['id', 'engine_type']
        ordering = ['engine_type']

class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = ['id', 'name']
        ordering = ['name']

class CarModelSerializer(serializers.ModelSerializer):
    make = CarMakeSerializer()
    class Meta:
        model = CarModel
        fields = ['id', 'name', 'make']
        ordering = ['name']

class CarSerializer(serializers.ModelSerializer):
    model = CarModelSerializer()
    engine = CarEngineSerializer()

    class Meta:
        model = Car
        fields = ['id', 'year', 'model', 'engine']
        ordering = ['year']