# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Lugares
from serializers import LugaresSerializer

import json

class LugaresTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.primer_lugar = Lugares.objects.create(
            calle = "principal",
            nombre = "Hospital Milenium",
            colonia = "La Marqueza",
            tipo_lugar = "Hospital"
        )
        self.segundo_lugar = Lugares.objects.create(
            calle = "segundaria",
            nombre = "Centro de Apocio Miguelito",
            colonia = "La Minerva",
            tipo_lugar = "Centro de Apocio"
        )
        self.lugar_correcto_json = {
            "calle" : "es un test",
            "nombre" : "Vivienda Test",
            "colonia" : "Colonia Test",
            "tipo_lugar" : "Lugar Test"
        }
        self.lugar_incorrecto_json = {
            "calle" : 35,
            "nombre" : "nombre del lugar Test",
            "colonia" : "Colonia  del lugar Test",
            "tipo_lugar" : "Lugar Test"
        }

    def test_get_all_lugares(self):
        response = self.client.get(reverse("lugares_end_point"))
        lugares = Lugares.objects.all()
        serializer = LugaresSerializer(lugares, many=True)
        self.assertEquals(response.status_code,200)
        self.assertEquals(serializer.data,response.data)

    # def test_get_persona(self):
    #     response = self.client.get(reverse("persona_end_point", kwargs={'pk':self.primera_persona.id}))
    #     persona = Personas.objects.get(pk=self.primera_persona.id)
    #     serializer = PersonasSerializer(persona)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertEquals(serializer.data, response.data)
    
    def test_post_lugares(self):
        response = self.client.post(reverse('lugares_end_point'), 
            data=json.dumps(self.lugar_correcto_json),
            content_type='application/json')
        self.assertEquals(response.status_code, 201)

    # def test_delete_persona(self):
    #     response = self.client.delete(reverse('persona_end_point', kwargs={'pk':self.segunda_persona.id}))
    #     self.assertEqual(response.status_code, 204)
    
    # def test_put_persona(self):
    #     persona = Personas.objects.get(pk=self.primera_persona.id)
    #     response = self.client.put(reverse('persona_end_point', kwargs={'pk':self.primera_persona.id}), 
    #         data=json.dumps(self.persona_correcta_json),
    #         content_type='application/json')
    #     self.assertEquals(response.status_code, 202)
        