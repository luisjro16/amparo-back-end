from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Paciente, Medicamento, Agendamento, RegistroMedicacao
from .serializers import PacienteSerializer, MedicamentoSerializer, AgendamentoSerializer, RegistroMedicacaoSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    serializer_class = PacienteSerializer
    permission_classes = [permissions.IsAuthenticated]

class MedicamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que medicamentos sejam vistos ou editados.
    """
    # O serializer que deve ser usado para converter os dados
    serializer_class = MedicamentoSerializer
    
    # Define que apenas usuários autenticados podem acessar este endpoint
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Esta view deve retornar uma lista de todos os medicamentos
        para o usuário atualmente autenticado.
        """
        # self.request.user é o objeto do usuário logado (o Paciente)
        return Medicamento.objects.filter(paciente=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        """
        Associa o medicamento que está sendo criado ao usuário logado.
        """
        # Ao salvar, passamos o paciente logado como o dono do medicamento.
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
