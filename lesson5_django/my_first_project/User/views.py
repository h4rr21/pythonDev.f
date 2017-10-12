# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny

from django.shortcuts import render
from .models import User
from .serializers import UserSerializer

import json
import requests


# Create your views here.
class UserApi(APIView):
    permission_classes = (AllowAny,)

    def _getUser(self, pk):
        return User.objects.get(pk=pk)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    def put(self, request, pk):
        user = self._getUser(pk)
        serializer = UserSerializer(user, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

    def delete(self, request, pk):
        user = self._getUser(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)