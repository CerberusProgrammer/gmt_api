# GMT API

GMT API es una API REST desarrollada con Django para generar rutas en Baja California.

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto:

1. Clona el repositorio:
    ```
    git clone https://github.com/CerberusProgrammer/gmt_api
    cd GMT_API
    ```

2. Instala las dependencias necesarias:
    ```
    pip install -r requirements.txt
    ```

3. Ejecuta el servidor:
    ```
    gunicorn gmt_api.wsgi:application
    ```

¡Y eso es todo! Ahora deberías tener tu API de Django ejecutándose localmente.