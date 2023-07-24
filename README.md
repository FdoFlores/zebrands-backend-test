Programas necesarios
python 3.9
docker desktop
NO TENER INSTALADO POSTGRESQL, ESTO BLOQUEARÍA EL PUERTO DE POSTGRESQL EN EL DOCKER.

Pasos
Duplicar el archivo ".env.example" y renombrar la copia con el nombre ".env"
Dentro del archivo .env modificar la variable llamada 'ADMIN_EMAIL' este correo es el que recibirá el admin que se seedea con el proyecto, recomiendo usar un correo propio para poder ver la notificación que se envía por correo.

#Crear virtual environment
python -m venv venv

#Activar virtual environment
./venv/Scripts/Activate.ps1

#Instalar dependencias
pip install -r requirements.txt

#Correr docker
docker-compose up -d

#Migraciones
python manage.py makemigrations
python manage.py migrate

#Inicializar variables
python manage.py seed_project

#Correr el proyecto
python manage.py runserver

Una vez que el programa esté iniciado, primero loguearse con el usuario:
username: admin
password: 12345

Para ver la pantalla de instrucciones.