# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#comentario

from django.db import models
from personas.models import Personas
#creat your models here

STATUS = (("1","Actual"),("0","Siempre NO"))

class Lugares(models.Model):
    calle = models.CharField(max_length=102)
    nombre = models.CharField(max_length=102)
    colonia = models.CharField(max_length=102)
    tipo_lugar = models.CharField(max_length=102)
    # muchos a muchos sin tabla relación
    # personas = models.ManyToManyField(Personas)

# lugarsito = Lugares.objects.create(calle="asdf", nombre="asdf", colonia="asdfff")
# lugarsito.save()
# personita ---> ya fue un objeto creado de persona
# lugarsito.add(personita)
# lugarsito.personas.create(parametros de persona)

class PersonasInLugares(models.Model):
    fecha = models.CharField(max_length=20)
    status = models.CharField(choices=STATUS, max_length=50)
    lugares_id = models.ForeignKey(Lugares)
    personas_id = models.ForeignKey(Personas)

