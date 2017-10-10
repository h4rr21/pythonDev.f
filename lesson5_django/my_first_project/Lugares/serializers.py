from rest_framework import serializers
from .models import Lugares


class GetLugares(serializers.Serializer):
    nombre = serializers.CharField(max_length=102)


class LugaresCreateSerializer(serializers.Serializer):
    calle = serializers.CharField(max_length=102)
    nombre = serializers.CharField(max_length=102)
    colonia = serializers.CharField(max_length=102)
    tipo_lugar = serializers.CharField(max_length=102)

    def create(self, validated_data):
        return Lugares.objects.create(**validated_data)

class LugaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugares
        fields = ['calle', 'nombre', 'colonia', 'tipo_lugar', 'id']

class LugaresModifySerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=102)

