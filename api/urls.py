# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicamentoViewSet, PacienteViewSet, AgendamentoViewSet, RegistroMedicacaoViewSet


router = DefaultRouter()

router.register(r'medicamentos', MedicamentoViewSet, basename='medicamento')
router.register(r'pacientes', PacienteViewSet, basename='paciente')
router.register(r'agendamentos', AgendamentoViewSet, basename='agendamento')
router.register(r'registrosmedicacao', RegistroMedicacaoViewSet, basename='registromedicacao')


urlpatterns = [
    path('', include(router.urls)),
]