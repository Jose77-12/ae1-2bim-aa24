# Platos Típicos de Ecuador

Esta es una aplicación Django para gestionar información sobre platos típicos de Ecuador. La aplicación permite agregar, editar y eliminar información sobre diferentes platos, incluyendo su nombre, descripción, ingredientes, precio y región de origen.

## Requisitos

- Python 3.x
- Django 3.x o superior

## Instalación

1. Clona el repositorio:

    ```sh
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Crea y activa un entorno virtual:

    ```sh
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:

    ```sh
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:

    ```sh
    python manage.py migrate
    ```

5. Crea un superusuario para acceder al panel de administración:

    ```sh
    python manage.py createsuperuser
    ```

6. Inicia el servidor de desarrollo:

    ```sh
    python manage.py runserver
    ```

7. Accede a la aplicación en tu navegador:

    ```sh
    http://127.0.0.1:8000/
    ```

## Uso

### Panel de Administración

Para acceder al panel de administración de Django, ve a:

GitHub Copilot
Aquí tienes un ejemplo de un archivo README.md para tu aplicación Django:

<http://127.0.0.1:8000/admin/>

Inicia sesión con el superusuario que creaste anteriormente. Desde el panel de administración, puedes gestionar los platos típicos de Ecuador.

### Modelos

La aplicación incluye el modelo `PlatosTipicosDeEcuador` con los siguientes campos:

- `nombre`: Nombre del plato (CharField)
- `descripcion`: Descripción del plato (TextField)
- `ingredientes`: Ingredientes del plato (TextField)
- `precio`: Precio del plato (DecimalField)
- `region`: Región de origen del plato (CharField)

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
****