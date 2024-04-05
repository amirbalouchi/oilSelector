from django.test import TestCase
from oil_selector_app.models.car import CarMake, CarModel, CarEngine, Car
from oil_selector_app.serializers.car import CarSerializer

class CarSerializerTests(TestCase):
    
    def setUp(self):
        self.make = CarMake.objects.create(name='Toyota')
        self.model = CarModel.objects.create(name='Corolla', make=self.make)
        self.engine = CarEngine.objects.create(engine_type='1.8L 4-Cylinder')
        self.car = Car.objects.create(year=2020, model=self.model, engine=self.engine)
        
        self.serializer = CarSerializer(instance=self.car)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'year', 'model', 'engine']))

    def test_engine_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['engine']['engine_type'], '1.8L 4-Cylinder')