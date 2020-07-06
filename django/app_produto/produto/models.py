from django.db import models
from django.utils import timezone


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome