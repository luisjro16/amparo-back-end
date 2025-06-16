# api/serializers.py

from rest_framework import serializers
from .models import Paciente, Medicamento, Agendamento, RegistroMedicacao

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        
class PacienteCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Paciente
        fields = ['username', 'password']
    
    def create(self, validated_data):
        username = validated_data['username']
        placeholder_email = f"{username.lower()}@amparo.app"
        if Paciente.objects.filter(email=placeholder_email).exists():
            raise serializers.ValidationError({"error": "Um erro inesperado ocorreu. Tente um nome de usuário diferente."})
        
        user = Paciente.objects.create_user(
            username=username,
            password=validated_data['password'],
            email=placeholder_email 
        )
        return user

class MedicamentoSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(read_only=True)

    class Meta:
        model = Medicamento
        
        fields = ['id', 'nome', 'dose', 'composto', 'meia_vida', 'descricao', 'paciente']
        
class AgendamentoSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(read_only=True)
    medicamento = MedicamentoSerializer(read_only=True)
    
    class Meta:
        model = Agendamento
        fields = ['id', 'horario']
        
class RegistroMedicacaoSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(read_only=True)
    agendamento = AgendamentoSerializer(read_only=True)
    
    class Meta:
        model = RegistroMedicacao
        fields = ['id', 'data_hora_tomada', 'tomou']