from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario(models.Model):
	nome = models.CharField(max_length=100)
	usuario = models.OneToOneField(User, on_delete=models.PROTECT)
	salario_liquido = models.DecimalField(max_digits=10,decimal_places=2)

	def __str__(self):
		return self.nome