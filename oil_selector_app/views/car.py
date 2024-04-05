from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers.car import *
from ..models.car import *

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