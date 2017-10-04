from rest_framework import serializers
from .models import Personas

SEXOS = (("M", "Mujer"), ("H", "Hombre"), ("I", "Indefinido"))
TIPOSPERSONAS = (("Voluntario", "Voluntario"), ("Damnificado", "Damnificado"), ("Otro", "Otro"))


def validarEdad(source):
    if source <= 100:
        pass
    else:
        serializers.ValidationError("Mas de 100 SEEEGUUUROOO ???")
        pass


class GetPersonas(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)


class PersonasCreateSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)
    edad = serializers.IntegerField(validators=[validarEdad])
    sexo = serializers.CharField(max_length=5)
    tipo_de_personas = serializers.CharField(max_length=50)


class PersonasModifySerializer(serializers.Serializer):
    tipo_de_personas = serializers.CharField(max_length=50)