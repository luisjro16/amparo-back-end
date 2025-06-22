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
    
    dosagem_formatada = serializers.CharField(read_only=True)

    class Meta:
        model = Medicamento

        fields = ['id', 'nome', 'dosagem_valor', 'dosagem_unidade', 'observacao', 'paciente', 'dosagem_formatada']

class AgendamentoSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(read_only=True)
    medicamento = MedicamentoSerializer(read_only=True)
    
    class Meta:
        model = Agendamento
        fields = ['id', 'horario', 'frequencia', 'paciente', 'medicamento', 'data_fim']
        
class RegistroMedicacaoSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(read_only=True)
    agendamento = AgendamentoSerializer(read_only=True)
    
    class Meta:
        model = RegistroMedicacao
        fields = ['id', 'data_hora_tomada', 'tomou']
        
class RegistroMedicacaoCreateSerializer(serializers.ModelSerializer):
    agendamento = serializers.PrimaryKeyRelatedField(queryset=Agendamento.objects.all())

    class Meta:
        model = RegistroMedicacao
        fields = ['agendamento', 'tomou', 'data_hora_tomada']
        
class MedicamentoComAgendamentoSerializer(serializers.Serializer):
    
    # Campos do Medicamento
    nome = serializers.CharField(max_length=255)
    dosagem_valor = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    dosagem_unidade = serializers.CharField(max_length=20, required=False)
    observacao = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    # Campos do Agendamento
    horario_inicio = serializers.TimeField()
    horario_fim = serializers.TimeField(required=False, allow_null=True)
    intervalo = serializers.IntegerField(min_value=1, max_value=24)
    duracao_valor = serializers.IntegerField(min_value=1, required=False, allow_null=True)
