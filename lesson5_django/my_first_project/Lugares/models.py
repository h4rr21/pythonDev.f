# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#comentario

from django.db import models

#creat your models here


class Lugares(models.Model):
    calle = models.CharField(max_length=102)
    nombre = models.CharField(max_length=102)
    colonia = models.CharField(max_length=102)
