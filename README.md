Sitio de Farmatodo
Este repositorio contiene el proyecto Django para Farmatodo, una solución integral para la gestión de una farmacia.

NOTA: El proyecto está guardado en un servidor Linux en AWS, por lo que si se quiere revisar el funcionamiento se tiene que encender el servidor y posteriormente generar las pruebas.

Intención: Generar una aplicación web que permita llevar la correcta gestión de las incidencias de mantenimiento en las distintas sucursales de una farmacia. 

Estructura del Proyecto
farmatodo_site: El directorio principal del proyecto Django.

PAGINA DE INICIO:
![image](https://github.com/Leonardo1278/FARMATODO-APP/assets/75225473/a25266e8-d303-40bf-85ca-291f035483bc)

INICIO DE SESIÓN: ![image](https://github.com/Leonardo1278/FARMATODO-APP/assets/75225473/cf1d39fb-9f34-4c90-9efe-bab190632467)

UNA VEZ INICIADA LA SESIÓN;

FORMULARIO: ![image](https://github.com/Leonardo1278/FARMATODO-APP/assets/75225473/9e7bc9e0-5a4f-477e-ba4f-6dcda1495e83)

INCIDENCIAS: ![image](https://github.com/Leonardo1278/FARMATODO-APP/assets/75225473/00c66ed6-e314-4ca7-87d7-a63a757580d4)

OVERVIEW: ![image](https://github.com/Leonardo1278/FARMATODO-APP/assets/75225473/dd0cf110-2d82-49c8-b7b7-0cf57a191721)

REGISTRAR USUARIO: ![image](https://github.com/Leonardo1278/FARMATODO-APP/assets/75225473/707a8ecc-a0db-4bac-867d-ca22db61207b)





__init__.py: Un archivo vacío que indica a Python que este directorio debe considerarse como un paquete.
asgi.py: Punto de entrada para servidores web compatibles con ASGI para desplegar el proyecto.
settings.py: Configuraciones del proyecto Django, incluyendo configuración de base de datos, internacionalización, y más.
urls.py: Las declaraciones de las URL para este proyecto Django; “la tabla de contenidos” de tu sitio web Django.
wsgi.py: Punto de entrada para servidores web compatibles con WSGI para desplegar el proyecto.
incidencias: Una aplicación Django dentro del proyecto, encargada de la gestión de incidencias.

migrations: Directorio que contiene las migraciones de la base de datos para esta aplicación.
templates: Directorio que contiene los templates HTML para esta aplicación.
admin.py: Configuración de la interfaz de administración de Django para la aplicación.
apps.py: Configuración de la aplicación de Django.
forms.py: Formularios de Django para la aplicación.
models.py: Modelos de Django para la aplicación, definiendo la estructura de datos.
tests.py: Pruebas para la aplicación.
views.py: Vistas de Django para la aplicación, controlando el flujo y la lógica.
manage.py: Una utilidad de línea de comandos que te permite interactuar con este proyecto Django de varias maneras.

Instalación
Para instalar y configurar tu entorno de desarrollo local, sigue estos pasos:

Clona el repositorio a tu máquina local.
Crea un entorno virtual para el proyecto.
Instala las dependencias utilizando pip install -r requirements.txt (deberás crear este archivo con las dependencias).
Configura tu archivo settings.py con la base de datos y otras configuraciones necesarias.
Realiza las migraciones de la base de datos con python manage.py migrate.
Ejecuta el servidor de desarrollo con python manage.py runserver.
