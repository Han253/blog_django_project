# Proyecto de Blog en Django 5

Este proyecto es una aplicación web de blog desarrollada en **Django 5** como parte del curso de **Programación en la Web** para estudiantes de 5º semestre de Ingeniería de Sistemas. Permite a los usuarios crear, editar y eliminar publicaciones, además de gestionar categorías y comentar en los artículos.

## Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

- **Python 3.10 o superior**
- **Django 5**
- **Git**
- **SQLite (base de datos por defecto de Django)**

## Instalación y configuración

### Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
```

### Crear y activar un entorno virtual

```bash
python -m venv env
source env/bin/activate  # En Linux/Mac
env\Scripts\activate  # En Windows
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Configurar la base de datos

```bash
python manage.py migrate
```

### Crear un superusuario (opcional, para acceder al panel de administración)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para establecer un nombre de usuario, correo electrónico y contraseña.

### Ejecutar el servidor

```bash
python manage.py runserver
```

Accede a la aplicación en: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Comandos comunes en Django

- **Iniciar el servidor de desarrollo:** `python manage.py runserver`
- **Aplicar migraciones:** `python manage.py migrate`
- **Crear una nueva aplicación:** `python manage.py startapp nombre_app`
- **Crear superusuario:** `python manage.py createsuperuser`
- **Revisar los modelos en la base de datos:** `python manage.py showmigrations`

## Estructura del Proyecto

```
/NOMBRE_DEL_PROYECTO/
│── manage.py              # Archivo principal de Django
│── requirements.txt       # Lista de dependencias
│── env/                   # Entorno virtual (no se sube a Git)
│── /modulo/               # Aplicación principal
│   │── models.py          # Modelos de la base de datos
│   │── views.py           # Lógica de las vistas
│   │── urls.py            # Definición de rutas
│   │── templates/         # Archivos HTML
│── /static/               # Archivos CSS y JS
│── db.sqlite3             # Base de datos SQLite (por defecto)
```

## Funcionalidades principales

- Registro e inicio de sesión de usuarios
- Creación, edición y eliminación de publicaciones
- Filtrado de publicaciones por categorías
- Gestión de comentarios en las publicaciones
- Interfaz administrativa con Django Admin

## Licencia

Este proyecto es de uso educativo y está bajo la licencia **MIT**.

---

🚀 ¡Feliz codificación! 😊

