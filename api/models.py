from django.db import models
from django.contrib.auth.models import AbstractUser

class Paciente(AbstractUser):
    email = models.EmailField(unique=True, blank=False) 
    
    
    def __str__(self):
        return self.username

class Medicamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='medicamentos')

    nome = models.CharField(max_length=255, null=False, blank=False)
    dosagem_valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    UNIDADE_CHOICES = [
        ('mg', 'mg'),
        ('g', 'g'),
        ('ml', 'ml'),
        ('gotas', 'gotas'),
        ('comprimido(s)', 'comprimido(s)'),
        ('cápsula(s)', 'cápsula(s)'),
    ]
    dosagem_unidade = models.CharField(max_length=20, choices=UNIDADE_CHOICES, default='mg')
    observacao = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def dosagem_formatada(self):
        if self.dosagem_valor and self.dosagem_unidade:
            return f"{self.dosagem_valor} {self.dosagem_unidade}"
        return ""
    
    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='agendamentos')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name='agendamentos')
    data_fim = models.DateField(null=True, blank=True)

    horario = models.TimeField(null=False, blank=False)
    
    FREQUENCIA_CHOICES = [
        ('Diário', 'Diário'),
        ('Semanal', 'Semanal'),
    ]
    frequencia = models.CharField(
        max_length=50,
        choices=FREQUENCIA_CHOICES,
        null=False,
        blank=False
    )   
    
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