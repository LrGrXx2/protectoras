from django.db import models
from django.db.models.base import Model

# Create your models here.
class Protectora(models.Model):
    nombre_protectora = models.CharField("Nombre protectora", max_length = 200)
    localizacion = models.CharField("Localizacion", max_length = 200, blank = True)

    def __str__(self):
        return f'{self.nombre_protectora}'

    class Meta:
        verbose_name = 'Protectora'
        verbose_name_plural = 'Protectoras'

#-------------------------------------------------------------------------

class Animal(models.Model):
    especie = models.CharField("Especia", max_length = 200)
    nombre_raza = models.CharField("Raza", max_length = 200)
    descripcion = models.CharField("Descripción", max_length = 200, blank = True)

    def __str__(self):
        return f'{self.especie} {self.nombre_raza}'

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'
        
#-------------------------------------------------------------------------

class Rescate(models.Model):
    nombre_animal = models.CharField("Nombre animal", max_length = 200)
    adoptado = models.CharField("En adopción", max_length = 200)

    # Relaciones
    nombre_protectora = models.ForeignKey('Protectora', on_delete = models.SET_NULL, null = True)
    especie = models.ForeignKey('Animal', on_delete = models.SET_NULL, null = True)
    nombre_raza = models.ForeignKey('Animal', on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return f'{self.nombre_animal} {self.last_name}'

    class Meta:
        verbose_name = 'Rescate'
        verbose_name_plural = 'Rescates'

        