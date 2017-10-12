# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework import status
from .models import Personas
from .serializers import PersonasSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import render
import json
import requests


# Create your views here.
class PersonasApi(APIView):
    def get(self, request):
        people = Personas.objects.all()
        serializer = PersonasSerializer(people, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PersonasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            self._sendPushNotification("Persona creada", "dl92-bxKmVg:APA91bHfbn-2RCSxShmxOVKgQPPOLU9-gvVsk5Wo4m2G2DEXfFSJ0C3wa5ro3eIxiyIwpFioZEW45Qf3IBHqhmUmK-w8sjnaWN-mPonqZCsiaWJSMBEUIdE8zYghZS4sMmqiDlTgw7-i")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    def _sendPushNotification(self, message, deviceToken):
        baseUrl = "https://fcm.googleapis.com/fcm/send"
        headers = {"Authorization": "key=AIzaSyB0k006LxEMxjpcL1bgz6CkAtEhX2UjQdY", "Content-Type": "application/json"}
        data = { 
            "notification": {
                "title": message,
                "body": "5 to 1",
                "icon": "firebase-logo.png",
                "click_action": "http://localhost:8081"
                },
                "to" : deviceToken
            }
        data = json.dumps(data)       
        pushNotification = requests.post(baseUrl, headers = headers, data=data)
        pushNotificationJson = pushNotification.json()
        #if pushNotification.status_code == 200:
        #    return False
        #else:
        #    return True
        if pushNotificationJson.__contains__("error"):
            return False
        else:
            return True

class PersonaApi(APIView):
    def _getPersona(self, pk):
        try:
            return Personas.objects.get(pk=pk)
        except Personas.DoesNotExist:
            raise NotFound("Neeel No existe!!")
    
    def get(self, request, pk):
        persona = self._getPersona(pk)
        serializer = PersonasSerializer(persona)
        return Response(serializer.data, status=status.HTTP_200_OK )

    def put(self, request, pk):
        persona = self._getPersona(pk)
        serializer = PersonasSerializer(persona, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

    def delete(self, request, pk):
        persona = self._getPersona(pk)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)