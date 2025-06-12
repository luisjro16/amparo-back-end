from django.db import models
from django.contrib.auth.models import AbstractUser

class Paciente(AbstractUser):
    email = models.EmailField(unique=True, blank=False) 
    
    
    def __str__(self):
        return self.username

class Medicamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='medicamentos')

    nome = models.CharField(max_length=255, null=False, blank=False)
    dose = models.CharField(max_length=100, null=False, blank=False)
    
    composto = models.CharField(max_length=255, null=True, blank=True)
    meia_vida = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='agendamentos')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name='agendamentos')

    horario = models.DateTimeField(null=False, blank=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Agendamento de {self.medicamento.nome} para {self.paciente.username} em {self.horario}"


class RegistroMedicacao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='registros_medicacao')
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE, related_name='registros_medicacao')

    data_hora_tomada = models.DateTimeField(null=False, blank=False)
    tomou = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Registros de Medicação"

    def __str__(self):
        status = "Tomou" if self.tomou else "Não tomou"
        return f"Registro de {self.agendamento.medicamento.nome} - {status}"