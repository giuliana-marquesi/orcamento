from django.contrib import admin
from .models import GastoPrevisto, GastoDiario, Categoria


# Register your models here.
admin.site.register(GastoPrevisto)
admin.site.register(GastoDiario)
#admin.site.register(Gasto)
admin.site.register(Categoria)
