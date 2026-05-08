from django.db import models

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    diagnostico = models.TextField()
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='pacientes'
    )

    def __str__(self):
        return self.nombre