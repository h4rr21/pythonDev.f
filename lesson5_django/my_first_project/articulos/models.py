# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#comentario

from django.db import models
#creat your models here


class Articulos(models.Model):
    nombre = models.CharField(max_length=102)