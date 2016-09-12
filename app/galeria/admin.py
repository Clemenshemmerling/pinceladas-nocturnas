from django.contrib import admin
from .models import Galeria
# Register your models here.
@admin.register(Galeria)
class AdminGaleria(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'descripcion', 'precio',)