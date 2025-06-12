# api/serializers.py

from rest_framework import serializers
from .models import Paciente, Medicamento, Agendamento, RegistroMedicacao

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class MedicamentoSerializer(serializers.ModelSerializer):
    # ModelSerializer é uma classe "mágica" que cria campos e validações
    # automaticamente a partir do seu modelo. Muito prático!
    
    # Para mostrar alguns dados do paciente, e não apenas o ID.
    # read_only=True significa que este campo não será exigido ao criar/atualizar um medicamento.
    paciente = PacienteSerializer(read_only=True)

    class Meta:
        model = Medicamento
        # Lista os campos que devem ser incluídos na representação JSON.
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