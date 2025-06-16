from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Paciente, Medicamento, Agendamento, RegistroMedicacao
from .serializers import PacienteSerializer, MedicamentoSerializer, AgendamentoSerializer, RegistroMedicacaoSerializer, PacienteCreateSerializer

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

    def get_queryset(self):
    
        return Medicamento.objects.filter(paciente=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        
        serializer.save(paciente=self.request.user)
        
class AgendamentoViewSet(viewsets.ModelViewSet):
    serializer_class = AgendamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Agendamento.objects.filter(paciente=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(paciente=self.request.user)
        
class RegistroMedicacaoViewSet(viewsets.ModelViewSet):
    serializer_class = RegistroMedicacaoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return RegistroMedicacao.objects.filter(paciente=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(paciente=self.request.user)
