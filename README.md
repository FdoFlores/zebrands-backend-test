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
username:admin
password:12345

# CREDENCIALES DE ADMINS
username: admin
password: 12345
username: admin2
password: 12345
# CREDENCIALES DE USER PUBLICO
username: anon
password: 12345

Para ver la pantalla de instrucciones.


###########################

Hola! para el flujo principal se debe loguear con el usuario administrador de esta aplicación web es primero crear una "Brand" despues un "Product" para que así los usuarios publicos puedan consultarlos
Me tomé la libertad de inventar un flujo muy basico y sencillo de compras, en las que los usuarios publicos entran a ver la lista de productos, presionan realizar una compra y toman el producto que desean comprar, creando así un "Buyout" cuando se realiza una compra se le notifica a los administradores y se les manda un correo con la información de la compra. Esto con el propósito de mantener el record de las veces que un usuario revisa o adquiere un producto, y con esta información se pueden realizar los reportes a futuro.

Además diseñé este front como ejemplo de fullstack en donde integro la api hecha con django rest framework y el frontend hecho con django.

Como administrador puedes ver, crear, editar y eliminar Brands, Products y Users. Los Buyouts solo pueden ser vistos, porque en teoría nadie debería hacer cambios a una compra porque podría comprometer la consistencia de la información. Cuando se modifica un product se le manda un correo a TODOS los administradores notificando esta acción. (en un futuro se podría mejorar el mensaje del correo enviado)

Como usuario publico puedes ver los productos y realizar una compra.

Limitantes en el sistema:
-El CRUD de users solo permite crear usuarios publicos, por falta de tiempo no logré terminar el flujo de permisos para administradores y usuarios, por lo tanto los usuarios con las credenciales "admin, 12345" y "admin2, 12345" son los unicos administradores, todos los usuarios creados con el CRUD de users son considerados usuarios publicos.

Mejoras que podrían integrarse en un futuro:
-Diseñar un flujo que guarde los precios de los productos de acuerdo a la fecha de la compra, actualmente se genera mucha información redundante ya que guardo el precio del producto que tenía en el momento que se realizó la compra por cada compra registrada, se me ocurrió que podría tener una tabla con los precios y su fecha de modificación, así podría quitar el campo de buyout_price de la compra y deducirla en base a la fecha en la que se generó la compra. Esto mejoraria la calidad y el tiempo de creación de los reportes.

-Tener un control de unidades que se haga en automatico con signals de Django, podría realizarse despues de que se mandan los correos, así se hace una vez por compra.

-En el CRUD de usuarios, poder manejar los permisos de los usuarios, permitiendo volver a un usuario administrador o usuario publico en cualquier momento. al igual que crear mas grupos con menos o mas permisos que los admins.

-Tener tablas de historicals y campos de auditoria, para tener registro de todas las compras y toda su información durante la linea del tiempo, de esta forma no perderiamos nunca la información modificada, por ejemplo si manejaramos historical en las compras, los administradores sí podrían modificarlas, porque sin importar que cambien aun podremos saber las unidades o el precio de una compra cuando recien fue registrada, con esto podriamos supervisar el trabajo de los administradores.

Links de documentación de la API: 
http://127.0.0.1:8000/api/create_buyout/
http://127.0.0.1:8000/api/update_buyout/id
http://127.0.0.1:8000/api/get_buyouts/
http://127.0.0.1:8000/api/delete_buyout/id
http://127.0.0.1:8000/api/create_brand/
http://127.0.0.1:8000/api/update_brand/id
http://127.0.0.1:8000/api/get_brands/
http://127.0.0.1:8000/api/delete_brand/id
http://127.0.0.1:8000/api/create_product/
http://127.0.0.1:8000/api/'update_product/id/
http://127.0.0.1:8000/api/get_products/
http://127.0.0.1:8000/api/delete_product/id
http://127.0.0.1:8000/api/create_user/
http://127.0.0.1:8000/api/update_user/id
http://127.0.0.1:8000/api/get_users/
http://127.0.0.1:8000/api/delete_user/id