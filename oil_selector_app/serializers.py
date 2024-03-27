# oil_selector_app/serializers.py

from rest_framework import serializers
from .models.product import Category, Product, ProductVariant, RecommendedProduct
from .models.car import Car, CarMake, CarModel, CarEngine

class CarEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarEngine
        fields = ['id', 'engine_type']

class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = ['id', 'name']

class CarModelSerializer(serializers.ModelSerializer):
    make = CarMakeSerializer()
    class Meta:
        model = CarModel
        fields = ['id', 'name', 'make']

class CarSerializer(serializers.ModelSerializer):
    model = CarModelSerializer()
    engine = CarEngineSerializer()

    class Meta:
        model = Car
        fields = ['id', 'year', 'model', 'engine']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'is_active', 'created_at']

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id', 'sku', 'unit']

class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description', 'image', 'external_url', 'variants', 'created_at']

class RecommendedProductSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    product = ProductSerializer()

    class Meta:
        model = RecommendedProduct
        fields = ['id', 'car', 'product', 'capacity', 'capacity_note', 'recommendation_note', 'created_at', 'updated_at']
