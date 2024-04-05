from rest_framework import generics
from ..models.product import *
from ..serializers.product import *

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all().order_by('priority')
    serializer_class = CategorySerializer

class RecommendedProductForCarAPIView(generics.ListAPIView):
    serializer_class = RecommendedProductSerializer

    def get_queryset(self):
        car_id = self.request.query_params.get('car_id', None)
        category_id = self.request.query_params.get('category_id', None)

        if car_id is not None and category_id is not None:
            return RecommendedProduct.objects.filter(car_id=car_id, product__category_id=category_id)
        else:
            return RecommendedProduct.objects.none()