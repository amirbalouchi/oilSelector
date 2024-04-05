from django.db import models
from .abstract_models import AbstractBaseModel

class CarMake(AbstractBaseModel):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class CarModel(AbstractBaseModel):
    name = models.CharField(max_length=255)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.make.name} - {self.name}"
    
class CarEngine(AbstractBaseModel):
    engine_type = models.CharField(max_length=255)
    
    def __str__(self):
        return self.engine_type
    
class Car(AbstractBaseModel):
    year = models.IntegerField()
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    engine = models.ForeignKey(CarEngine, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.model.make.name} - {self.model.name} - {self.year}"