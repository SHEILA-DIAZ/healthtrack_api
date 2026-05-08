from rest_framework import viewsets
from .models import Paciente, Doctor
from .serializers import PacienteSerializer, DoctorSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    search_fields = ['nombre', 'diagnostico']


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer