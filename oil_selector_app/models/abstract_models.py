# oil_selector_app/models/abstract_models.py

from django.db import models
from django.utils import timezone

class AbstractBaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)
    priority = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
