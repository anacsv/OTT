from django.shortcuts import render
from .models import Categoria
from rest_framework import viewsets
from .serializers import CategoriaSerializer

class MarcaViewSet(viewsets.ModelViewSet):
   
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
