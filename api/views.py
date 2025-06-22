from django.shortcuts import render

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Paciente, Medicamento, Agendamento, RegistroMedicacao
from .serializers import PacienteSerializer, MedicamentoSerializer, AgendamentoSerializer, RegistroMedicacaoSerializer, PacienteCreateSerializer, MedicamentoComAgendamentoSerializer, RegistroMedicacaoCreateSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    
    def get_serializer_class(self):
        if self.action == 'create':
            return PacienteCreateSerializer
        return PacienteSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    

class MedicamentoViewSet(viewsets.ModelViewSet):
    
    serializer_class = MedicamentoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = MedicamentoComAgendamentoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        # objeto Medicamento
        medicamento = Medicamento.objects.create(
            paciente=request.user,
            nome=validated_data['nome'],
            dosagem=validated_data.get('dosagem', ''),
            observacao=validated_data.get('observacao', '')
        )

        # objeto Agendamento
        agendamento = Agendamento.objects.create(
            paciente=request.user,
            medicamento=medicamento,
            horario=validated_data['horario'],
            frequencia=validated_data['frequencia']
        )
        
        medicamento_data = MedicamentoSerializer(medicamento).data
        agendamento_data = AgendamentoSerializer(agendamento).data
        
        response_data = {
            'medicamento': medicamento_data,
            'agendamento': agendamento_data
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

class AgendamentoViewSet(viewsets.ModelViewSet):
    serializer_class = AgendamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Agendamento.objects.filter(paciente=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(paciente=self.request.user)
        
# class RegistroMedicacaoViewSet(viewsets.ModelViewSet):
#     serializer_class = RegistroMedicacaoSerializer
#     permission_classes = [permissions.IsAuthenticated]
    
#     def get_queryset(self):
#         return RegistroMedicacao.objects.filter(paciente=self.request.user).order_by('-created_at')

#     def perform_create(self, serializer):
#         serializer.save(paciente=self.request.user)
        
class RegistroMedicacaoViewSet(viewsets.ModelViewSet):
    queryset = RegistroMedicacao.objects.all()
    serializer_class = RegistroMedicacaoCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RegistroMedicacao.objects.filter(paciente=self.request.user)

    def perform_create(self, serializer):
        serializer.save(paciente=self.request.user)
