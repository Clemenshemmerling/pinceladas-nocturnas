from django.db import models

class Galeria(models.Model):
	nombre = models.CharField(max_length=255)
	imagen = models.ImageField(blank = True)
	descripcion = models.CharField(max_length=255)
	precio = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return self.nombre