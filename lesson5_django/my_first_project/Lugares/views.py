# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework import status
from .models import Lugares, PersonasInLugares
from .serializers import LugaresSerializer, PersonasInLugaresSerializaer
from rest_framework.response import Response

from django.shortcuts import render


# Create your views here.
class LugaresApi(APIView):
    def get(self, request):
        lugares = Lugares.objects.all()
        serializer = LugaresSerializer(lugares, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, info):
        serializer = LugaresSerializer(data=info.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonasInLugaresApi(APIView):
    def get (self, request):
        personasinlugares = PersonasInLugares.objects.all()
        serializer = PersonasInLugaresSerializaer (personasinlugares, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    def post(self, info):
        serializer = PersonasInLugares (data=info.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

''' class PersonaTodosLugares(APIView):
    def _getLugares(self, pk):
        try:
            return PersonasInLugares.objects.get(personas_id_id=pk)
        except PersonasInLugares.DoesNotExist:

            
        lugaresdePersona = PersonasInLugares.objects.get(pk)




    def _getPersona(self, pk):
        try:
            return Personas.objects.get(pk=pk)
        except Personas.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        persona = self._getPersona(pk)
        serializer = PersonasSerializer(persona)
        return Response(serializer.data, status=status.HTTP_200_OK ) '''