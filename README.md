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
git clone URL_DEL_REPOSITORIO
cd healthtrack_api
python -m venv venv
venv\Scripts\activate
pip install django djangorestframework django-filter
python manage.py migrate
python manage.py runserver