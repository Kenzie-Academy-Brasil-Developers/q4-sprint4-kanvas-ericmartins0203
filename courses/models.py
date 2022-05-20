from django.db import models
import uuid

class Courses(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True)
    link_repo = models.CharField(max_length=255)
    demo_time = models.TimeField()
    created_at = models.DateField(auto_now_add=True)

    instructor = models.OneToOneField(
        "accounts.MyUser", on_delete=models.CASCADE, null=True
    )
    students = models.ManyToManyField(
        "accounts.MyUser", related_name='student'
    )