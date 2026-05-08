# HealthTrack API

API REST desarrollada con Django y Django REST Framework para gestionar pacientes y doctores.

## Tecnologías usadas

- Python
- Django
- Django REST Framework
- SQLite
- django-filter

## Instalación

```bash
git clone https://github.com/SHEILA-DIAZ/healthtrack_api.git
cd healthtrack_api
python -m venv venv
venv\Scripts\activate
pip install django djangorestframework django-filter
python manage.py migrate
python manage.py runserver
```

## Endpoints

### Pacientes

- GET `/api/pacientes/`
- POST `/api/pacientes/`
- GET `/api/pacientes/{id}/`
- PUT `/api/pacientes/{id}/`
- PATCH `/api/pacientes/{id}/`
- DELETE `/api/pacientes/{id}/`

### Ejemplo POST Paciente

```json
{
  "nombre": "Ana Torres",
  "edad": 32,
  "diagnostico": "Hipertensión",
  "doctor": 1
}
```

### Doctores

- GET `/api/doctores/`
- POST `/api/doctores/`
- GET `/api/doctores/{id}/`
- PUT `/api/doctores/{id}/`
- PATCH `/api/doctores/{id}/`
- DELETE `/api/doctores/{id}/`

### Ejemplo POST Doctor

```json
{
  "nombre": "Carlos Mendoza",
  "especialidad": "Cardiología"
}
```

## Búsqueda

```bash
/api/pacientes/?search=Ana
/api/pacientes/?search=Hipertensión
```

## Relación

Cada paciente está relacionado con un doctor.

La respuesta del endpoint de pacientes muestra:

- doctor_nombre
- doctor_especialidad