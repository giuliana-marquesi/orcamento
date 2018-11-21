from django.db import models
from categoria.models import Categoria


# Create your models here.
class Previsto(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    credito = models.BooleanField()

    def __str__(self):
        return self.nome
