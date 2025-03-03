# Django CRUD de Tareas App con Docker Compose

Este proyecto es una aplicación CRUD de Tareas en Django, configurada para ejecutarse con Docker Compose y Nginx como proxy inverso.

## 🚀 Tecnologías utilizadas

<p align="center">
  <img src="https://rathank.com/wp-content/uploads/2022/09/django.png" alt="Django" width="50" height="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" alt="PostgreSQL" width="50" height="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nginx/nginx-original.svg" alt="Nginx" width="50" height="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" alt="Docker" width="50" height="50"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Tailwind_CSS_Logo.svg/1024px-Tailwind_CSS_Logo.svg.png" alt="Tailwind" width="60" height="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" alt="Git" width="50" height="50"/>
</p>

## 📌 Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalados:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 🚀 Pasos para ejecutar el proyecto

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/django_crud_app.git
cd django_crud_app

# 2. Construir y levantar los contenedores
docker-compose up

# 3. Crear un superusuario (opcional, para acceder al panel de administración)
docker exec -it django-crud-app python manage.py createsuperuser
```

## 🌍 Acceder a la aplicación

- Aplicación: [http://localhost:8080/crud](http://localhost:8080/crud)
- Panel de administración: [http://localhost:8080/admin](http://localhost:8080/admin)
- pgAdmin: [http://localhost:5050](http://localhost:5050)

## 🛠 Cómo acceder a pgAdmin y conectarse a PostgreSQL

1. Abre [http://localhost:5050](http://localhost:5050) en tu navegador.
2. Inicia sesión con las credenciales:
   - **Correo:** `admin@admin.com`
   - **Contraseña:** `admin`
3. Una vez dentro, haz clic en "Add New Server".
4. En la pestaña "General":
   - Nombre: `PostgreSQL`
5. En la pestaña "Connection":
   - Host: `db`
   - Port: `5432`
   - Maintenance database: `crud_db`
   - Username: `postgres`
   - Password: `postgres`

## 📂 Estructura del proyecto

```bash
.
├── django_crud_app/       # Código fuente de la aplicación
├── Dockerfile             # Configuración de la imagen de Django
├── docker-compose.yml     # Configuración de los servicios Docker
├── nginx.conf             # Configuración de Nginx como proxy
├── requirements.txt       # Dependencias de Python
├── entrypoint.sh          # Script de inicialización de Django
└── README.md              # Guía de uso del proyecto
```

## 📌 Notas

- Los archivos estáticos y de medios se almacenan en volúmenes Docker.
- Nginx actúa como proxy inverso, por lo que la aplicación se accede desde `localhost:8080`.
- pgAdmin está disponible en `localhost:5050`, con el usuario y contraseña definidos en `docker-compose.yml`.

## 📸 Capturas del proyecto

![image](https://github.com/user-attachments/assets/97fd940b-5a12-4565-ba98-029e16129970)

![image](https://github.com/user-attachments/assets/cc06b04c-fff0-446a-a008-857b01bc2dbd)

![image](https://github.com/user-attachments/assets/4e41e956-7230-4741-8ac6-2c4aede56b09)

¡Listo! Tu aplicación está funcionando con Docker Compose y Nginx. 🚀

