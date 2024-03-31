# oil_selector_app/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models.product import Category, RecommendedProduct
from .serializers import *
from .models.car import Car, CarMake, CarModel

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all().order_by('priority')
    serializer_class = CategorySerializer

class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all().order_by('year')
    serializer_class = CarSerializer

class CarMakeListAPIView(generics.ListAPIView):
    queryset = CarMake.objects.order_by('name')
    serializer_class = CarMakeSerializer

class CarModelListAPIView(generics.ListAPIView):
    serializer_class = CarModelSerializer

    def get_queryset(self):
        maker_id = self.request.query_params.get('maker_id', None)
        return CarModel.objects.filter(make_id=maker_id).order_by('name')

class CarYearListAPIView(APIView):
    def get(self, request,):
        model_id = request.query_params.get('model_id', None)
        cars = Car.objects.filter(model_id=model_id).values('id', 'year').distinct().order_by('year')
        return Response({'cars': cars})

class RecommendedProductForCarAPIView(generics.ListAPIView):
    serializer_class = RecommendedProductSerializer

    def get_queryset(self):
        car_id = self.request.query_params.get('car_id', None)
        category_id = self.request.query_params.get('category_id', None)

        if car_id is not None and category_id is not None:
            return RecommendedProduct.objects.filter(car_id=car_id, product__category_id=category_id)
        else:
            return RecommendedProduct.objects.none()