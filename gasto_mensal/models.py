from datetime import date
from django.db import models
from usuario.models import Usuario

# Create your models here.

class Categoria(models.Model):
	nome = models.CharField(max_length=70)

	def __str__(self):
		return self.nome


'''
class Gasto(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
'''

class GastoDiario(models.Model):
	#gasto = models.OneToOneField(Gasto, on_delete=models.CASCADE)
	data = models.DateField(auto_now=True)
	nome = models.CharField(max_length=200)
	valor = models.DecimalField(max_digits=5, decimal_places=2)
	categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True, blank=True)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome

class GastoPrevisto(models.Model):
	#gasto = models.OneToOneField(Gasto, on_delete=models.CASCADE)
	forma_pgnto = models.BooleanField()
	nome = models.CharField(max_length=200)
	valor = models.DecimalField(max_digits=5, decimal_places=2)
	categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True, blank=True)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


	def __str__(self):
		return self.nome
