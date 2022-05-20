from django.db import models
import uuid

class Address(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    street = models.CharField(max_length=255)
    house_number = models.FloatField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)
