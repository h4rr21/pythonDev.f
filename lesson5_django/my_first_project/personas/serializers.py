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

    def create(self, validated_data):
        return Personas.objects.create(**validated_data)

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ['nombre', 'edad', 'sexo', 'tipo_de_personas', 'id']
        
    def validate_edad(self, source):
        if source <= 100:
            return source
            pass
        else:
            raise serializers.ValidationError("Mas de 100 SEEEGUUUROOO ???")
            pass

class PersonasModifySerializer(serializers.Serializer):
    tipo_de_personas = serializers.CharField(max_length=50)

