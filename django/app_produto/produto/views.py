from django.shortcuts import render
from .models import Produto
from rest_framework import viewsets
from .serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
   
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
