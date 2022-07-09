from django.http import HttpResponse
from mainloop.models import Camera
from mainloop.serializers import CameraSerializer
from rest_framework import generics
  
def index(request):
    return HttpResponse("<h2>Главная</h2><h3>Новый текст</h3>")
 
def about(request):
    return HttpResponse("<h2>О сайте</h2>")
 
def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

class CameraApiView(generics.ListAPIView):
    queryset  = Camera.objects.all()
    serializer_class = CameraSerializer

