# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#comentario

from django.db import models

SEXOS = (("M", "Mujer"), ("H", "Hombre"), ("I", "Indefinido"))
TIPOSPERSONAS = (("Voluntario", "Voluntario"), ("Damnificado", "Damnificado"), ("Otro", "Otro"))
#creat your models here


class Personas(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField(max_length=3)
    sexo = models.CharField(choices=SEXOS, max_length=5)
    tipo_de_personas = models.CharField(choices=TIPOSPERSONAS, max_length=50)