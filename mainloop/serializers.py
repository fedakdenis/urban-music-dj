from mainloop.models import Camera 
from rest_framework import serializers


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ['name', 'group', 'uid', 'url', 'description', 'date_created', 'date_updated', 'is_active']