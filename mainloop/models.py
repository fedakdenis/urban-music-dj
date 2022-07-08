import uuid
from django.db import models

class Camera(models.Model):
    name = models.CharField(max_length=255, unique=True)
    group = models.CharField(max_length=255)
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    url = models.URLField()
    description = models.TextField(null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

