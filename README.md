# LAB03-EMPRESARIALES
EncuestaApp
EncuestaApp es una aplicación web desarrollada con Django que permite crear encuestas, votar en ellas y ver los resultados.

Requisitos Previos
Antes de instalar y configurar la aplicación, asegúrate de tener lo siguiente:

Python 3.8 o superior.
pip (administrador de paquetes de Python).
Un entorno virtual (recomendado).
Instalación
1. Clonar el Repositorio
Clona este repositorio en tu máquina local:

bash
Copiar código
git clone https://github.com/tu_usuario/EncuestaApp.git
cd EncuestaApp
2. Crear un Entorno Virtual
Crea y activa un entorno virtual para el proyecto:

bash
Copiar código
python -m venv entornito
source entornito/bin/activate   # En Windows usa `entornito\Scripts\activate`
3. Instalar Dependencias
Instala las dependencias requeridas usando pip:

bash
Copiar código
pip install -r requirements.txt
4. Configurar la Base de Datos
Asegúrate de que tienes configurada una base de datos SQLite por defecto en settings.py. Si deseas utilizar otra base de datos (como PostgreSQL, MySQL, etc.), actualiza la configuración en settings.py en la sección DATABASES.

5. Aplicar Migraciones
Aplica las migraciones para configurar la base de datos:

bash
Copiar código
python manage.py migrate
6. Crear un Superusuario
Crea un superusuario para acceder al panel de administración de Django:

bash
Copiar código
python manage.py createsuperuser
7. Cargar Datos Iniciales (Opcional)
Si tienes un archivo de datos iniciales (por ejemplo, fixtures), puedes cargarlo con:

bash
Copiar código
python manage.py loaddata nombre_del_fixture.json
Uso
1. Ejecutar el Servidor de Desarrollo
Para iniciar el servidor de desarrollo, ejecuta:

bash
Copiar código
python manage.py runserver
Accede a la aplicación en tu navegador en http://127.0.0.1:8000/.

2. Navegar por la Aplicación
Página de Inicio: Aquí se listarán todas las preguntas disponibles.
Detalle de Pregunta: Haz clic en una pregunta para ver sus opciones y votar.
Resultados: Después de votar, podrás ver los resultados de la encuesta.
3. Acceso al Administrador de Django
Puedes acceder al panel de administración en http://127.0.0.1:8000/admin/ usando las credenciales del superusuario que creaste anteriormente. Desde allí, puedes administrar las encuestas y opciones.

Despliegue en Producción
Para desplegar la aplicación en un entorno de producción, sigue estos pasos:

Configura tu servidor web (por ejemplo, Nginx o Apache) y un servidor de aplicaciones WSGI (como Gunicorn o uWSGI).
Asegúrate de que DEBUG esté configurado en False en el archivo settings.py.
Configura una base de datos en producción (como PostgreSQL) y actualiza las configuraciones de base de datos en settings.py.
Configura el almacenamiento estático y de archivos multimedia.
Utiliza un entorno virtual y asegúrate de que todas las dependencias estén instaladas.
Contribuciones
Si deseas contribuir al proyecto, por favor abre un issue o envía un pull request.

Licencia
Este proyecto está licenciado bajo la Licencia MIT.

