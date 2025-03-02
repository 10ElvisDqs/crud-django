FROM python:3.10-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalamos las dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    gcc \
    netcat-openbsd \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiamos el archivo requirements.txt desde el directorio local
COPY ./requirements.txt ./

# Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todos los archivos de tu proyecto al contenedor
COPY . /app/

# Exponemos el puerto 8000 para el servidor
EXPOSE 8000

# Comando para iniciar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
