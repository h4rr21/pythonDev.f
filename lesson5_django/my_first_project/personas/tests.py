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
            sexo="M",
            tipo_de_personas="Otro"
            )
        self.segunda_persona = Personas.objects.create(
            nombre="Safot",
            edad=50,
            sexo="I",
            tipo_de_personas="Voluntario"
            )
        self.persona_incorrecta_json = {
            "nombre":"Eduardod",
            "edad":14,
            "sexo":5,
            "tipo_de_personas":"Otro"
        }
        self.persona_correcta_json = {
            "nombre" :"Eduardod",
            "edad":"56",
            "sexo":"M",
            "tipo_de_personas":"Otro"
        }

        

    def test_get_all_personas(self):
        response = self.client.get(reverse("personas_end_point"))
        personas = Personas.objects.all()
        serializer = PersonasSerializer(personas, many=True)
        self.assertEquals(response.status_code,200)
        self.assertEquals(serializer.data,response.data)

    def test_get_persona(self):
        response = self.client.get(reverse("persona_end_point", kwargs={'pk':self.primer_persona.id}))
        persona = Personas.objects.get(pk=self.primer_persona.id)
        serializer = PersonasSerializer(persona)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(serializer.data, response.data)
    
    def test_post_persona(self):
        response = self.client.post(reverse('personas_end_point'), 
            data=json.dumps(self.persona_correcta_json),
            content_type='application/json')
        self.assertEquals(response.status_code, 201)
# Create your tests here.
