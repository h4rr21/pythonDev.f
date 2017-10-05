from rest_framework import serializers
from .models import Articulos


class GetArticulos(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)


class ArticulosCreateSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Articulos.objects.create(**validated_data)


class ArticulosModifySerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=50)

