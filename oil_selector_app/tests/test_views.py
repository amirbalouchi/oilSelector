from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from oil_selector_app.models.car import CarMake, CarModel, CarEngine, Car

class CarViewTests(APITestCase):

    def setUp(self):
        self.make = CarMake.objects.create(name='Toyota')
        self.model = CarModel.objects.create(name='Corolla', make=self.make)
        self.engine = CarEngine.objects.create(engine_type='1.8L 4-Cylinder')
        self.car = Car.objects.create(year=2020, model=self.model, engine=self.engine)

    def test_car_list_api_view(self):
        url = reverse('car-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)