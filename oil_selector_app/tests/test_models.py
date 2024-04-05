from django.test import TestCase
from oil_selector_app.models.car import CarMake, CarModel, CarEngine, Car

class CarModelTests(TestCase):
    
    def setUp(self):
        self.make = CarMake.objects.create(name='Toyota')
        self.model = CarModel.objects.create(name='Corolla', make=self.make)
        self.engine = CarEngine.objects.create(engine_type='1.8L 4-Cylinder')
        self.car = Car.objects.create(year=2020, model=self.model, engine=self.engine)

    def test_car_make_str(self):
        self.assertEqual(str(self.make), 'Toyota')

    def test_car_model_str(self):
        self.assertEqual(str(self.model), 'Toyota - Corolla')

    def test_car_engine_str(self):
        self.assertEqual(str(self.engine), '1.8L 4-Cylinder')

    def test_car_str(self):
        self.assertEqual(str(self.car), 'Toyota - Corolla - 2020')
