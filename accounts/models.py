import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(max_length=255, unique=True)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=150, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    address = models.ForeignKey("address.Address", on_delete=models.CASCADE, related_name='users', null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
