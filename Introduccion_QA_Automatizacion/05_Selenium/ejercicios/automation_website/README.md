# Proyecto de Automatización con Selenium

Este proyecto utiliza Python y Selenium para automatizar pruebas en navegadores web. Sigue los pasos a continuación para configurar tu entorno de desarrollo.

## Prerrequisitos

- Asegúrate de tener Python 3.x instalado. Puedes descargar Python desde [python.org](https://www.python.org/downloads/).

## Configuración del Entorno

1. **Crea un entorno virtual (venv):**

    En Windows:

    ```bash
    python -m venv venv
    ```

    En macOS/Linux:

    ```bash
    python3 -m venv venv
    ```

3. **Activa el entorno virtual:**

    En Windows:

    ```bash
    venv\Scripts\activate
    ```

    En macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

4. **Instala las dependencias:**
> asegurarse de estar en el virtual env antes de ejecutar esto (si seguiste los pasos deberias ya estar)

    ```bash
    pip install requirements.txt
    ```

## Ejecutar Pruebas

Después de configurar el entorno, puedes ejecutar las pruebas utilizando `pytest`:

```bash
pytest
```

Puede ejecutar tambien las pruebas desde vs code

