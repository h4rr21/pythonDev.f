# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework import status
from .models import Personas
from .serializers import PersonasCreateSerializer, GetPersonas
from rest_framework.response import Response

from django.shortcuts import render


# Create your views here.
class PersonasApi(APIView):
    def get(self, request):
        people = Personas.objects.all()
        serializer = GetPersonas(people, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, info):
        serializer = PersonasCreateSerializer(data=info.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


