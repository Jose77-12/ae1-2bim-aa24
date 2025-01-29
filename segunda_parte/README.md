# Platos Típicos de Ecuador - Segunda Parte

Esta es una aplicación de Python que implementa interfaces gráficas utilizando el patrón de diseño Modelo-Vista-Controlador (MVC) para gestionar información sobre platos típicos de Ecuador. La aplicación permite agregar, editar y eliminar información sobre diferentes platos, incluyendo su nombre, descripción, ingredientes, precio y región de origen.

## Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas y archivos:

- **controllers/**: Contiene los controladores de la aplicación.
  - `__init__.py`: Marca el directorio como un paquete.
  - `main_controller.py`: Controlador principal que maneja la lógica de la aplicación.

- **models/**: Contiene los modelos de datos.
  - `__init__.py`: Marca el directorio como un paquete.
  - `plato_model.py`: Modelo que representa la estructura de un plato típico.

- **views/**: Contiene las vistas de la aplicación.
  - `__init__.py`: Marca el directorio como un paquete.
  - `main_view.py`: Vista principal que crea la interfaz gráfica de usuario.

- `app.py`: Punto de entrada de la aplicación que inicializa la vista y el controlador.

## Requisitos

- Python 3.x
- Bibliotecas necesarias para la interfaz gráfica (por ejemplo, Tkinter, PyQt, etc.)

## Instalación

1. Clona el repositorio:

    ```sh
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio/segunda_parte
    ```

2. Instala las dependencias necesarias (si las hay).

3. Ejecuta la aplicación:

    ```sh
    python app.py
    ```

## Uso

La aplicación permite gestionar platos típicos de Ecuador a través de una interfaz gráfica. Puedes:

- Ver la lista de platos.
- Añadir un nuevo plato.
- Editar un plato existente.
- Eliminar un plato.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.