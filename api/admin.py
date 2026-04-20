# api/admin.py
from django.contrib import admin
from .models import Paciente, Medicamento, Agendamento, RegistroMedicacao

# Registra o modelo Paciente para que ele apareça no site de admin
admin.site.register(Paciente)

# Você pode registrar os outros modelos também!
admin.site.register(Medicamento)
admin.site.register(Agendamento)
admin.site.register(RegistroMedicacao)