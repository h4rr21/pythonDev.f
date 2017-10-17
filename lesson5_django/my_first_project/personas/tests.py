# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Personas
from serializers import PersonasSerializer

import json

class PersonasTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.primer_persona = Personas.objects.create(
            nombre="Juan Carlos",
            edad=35,
            tipo_de_personas="Otro"
            )
        self.primer_persona = Personas.objects.create(
            nombre="Safot",
            edad=50,
            tipo_de_personas="Voluntario"
            )
        

    def test_get_all_personas(self):
        response = self.client.get(reverse("personas_end_point"))
        personas = Personas.objects.all()
        serializer = PersonasSerializer(personas, many=True)
        self.assertEquals(response.status_code,200)
        self.assertEquals(serializer.data,response.data)
    

# Create your tests here.
