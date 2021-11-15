from django.db import models
from django.db.models.base import Model

# Create your models here.
class Protectora(models.Model):
    nombre_protectora = models.CharField("Nombre protectora", max_length = 200)
    direccion = models.CharField("Dirección", max_length = 200, blank = True)
    ciudad = models.CharField("Ciudad", max_length = 200, blank = True)
    coordenadas = models.CharField("Coordenadas", max_length = 500, blank = True)

    def __str__(self):
        return f'{self.nombre_protectora} {self.ciudad} {self.direccion}'

    class Meta:
        verbose_name = 'Protectora'
        verbose_name_plural = 'Protectoras'

#-------------------------------------------------------------------------

class Animal(models.Model):
    especie = models.CharField("Especia", max_length = 200)
    nombre_raza = models.CharField("Raza", max_length = 200)
    descripcion_animal = models.CharField("Descripción general", max_length = 500, blank = True)

    def __str__(self):
        return f'{self.especie} {self.nombre_raza}'

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'
        
#-------------------------------------------------------------------------

class Rescate(models.Model):
    nombre_animal = models.CharField("Nombre animal", max_length = 200)
    adoptado = models.CharField("En adopción", max_length = 200)
    descripcion_rescate = models.CharField("Descripción de este animal", max_length = 500, blank = True)

    # Relaciones
    nombre_protectora = models.ForeignKey('Protectora', on_delete = models.SET_NULL, null = True)
    especie = models.ForeignKey('Animal', on_delete = models.SET_NULL, null = True)
    nombre_raza = models.ForeignKey('Animal', on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return f'{self.nombre_animal} {self.last_name}'

    class Meta:
        verbose_name = 'Rescate'
        verbose_name_plural = 'Rescates'

        