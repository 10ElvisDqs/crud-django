#!/bin/bash

# Esperar a que la base de datos esté lista
echo "Esperando a que la base de datos esté lista..."
while ! nc -z django-crud-db 5432; do
  sleep 1
done
echo "Base de datos lista."

# Ejecutar las migraciones
echo "Aplicando migraciones..."
python manage.py migrate

# Cargar los datos iniciales
echo "Cargando datos iniciales..."
python manage.py loaddata initial_data.json

# Iniciar el servidor Django
echo "Iniciando servidor Django..."
python manage.py runserver 0.0.0.0:8000
