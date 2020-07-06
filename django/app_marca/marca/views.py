from django.shortcuts import render
from .models import Marca
from rest_framework import viewsets
from .serializers import MarcaSerializer

class MarcaViewSet(viewsets.ModelViewSet):
   
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
