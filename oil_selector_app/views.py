# oil_selector_app/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models.product import Category, RecommendedProduct
from .serializers import *
from .models.car import Car, CarMake, CarModel

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarMakeListAPIView(generics.ListAPIView):
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer

class CarModelListAPIView(generics.ListAPIView):
    serializer_class = CarModelSerializer

    def get_queryset(self):
        maker_id = self.request.query_params.get('maker_id', None)
        return CarModel.objects.filter(make_id=maker_id)

class CarYearListAPIView(APIView):
    def get(self, request,):
        model_id = request.query_params.get('model_id', None)
        car_years = Car.objects.filter(model_id=model_id).values_list('year', flat=True).distinct()
        return Response({'years': car_years})

class RecommendedProductForCarAPIView(generics.ListAPIView):
    serializer_class = RecommendedProductSerializer

    def get_queryset(self):
        car_id = self.request.query_params.get('car_id', None)
        category_id = self.request.query_params.get('category_id', None)

        if car_id is not None and category_id is not None:
            return RecommendedProduct.objects.filter(car_id=car_id, product__category_id=category_id)
        else:
            return RecommendedProduct.objects.none()