# Tarea: Automatización de Pruebas API

## Objetivo

Desarrollar una serie de pruebas automatizadas para una API RESTful utilizando `requests` y `assertpy`. La API utilizada será [ReqRes API](https://reqres.in/api-docs/#/default/get__resource_).

## Instrucciones

1. **Configura el entorno de pruebas:**

   Asegúrate de tener `requests` y `assertpy` instalados en tu entorno. Puedes instalarlos usando los siguientes comandos:

   ```bash
   pip install requests assertpy
   ```

2. **Crea un archivo de pruebas:**

   Crea un archivo llamado `test_api.py` en tu proyecto. Este archivo contendrá todas las pruebas para las diferentes operaciones de la API.

3. **Implementa las pruebas:**

   Escribe pruebas unitarias para las siguientes operaciones:
   - **Obtener una lista de usuarios (`GET /users`)**
     - Verifica que la respuesta tenga un código de estado 200.
     - Asegúrate de que la respuesta contenga una lista de usuarios.
     - Comprueba que la lista no esté vacía.
     - Valida que cada usuario en la lista tenga campos como `id`, `email`, `first_name`, `last_name`, y `avatar`.
   - **Crear un nuevo usuario (`POST /users`)**
     - Verifica que la respuesta tenga un código de estado 201.
     - Asegúrate de que la respuesta contenga los datos del usuario creado, incluyendo `id` y `createdAt`.
     - Prueba la creación de un usuario sin nombre para verificar el manejo de errores.

   - **Actualizar un usuario existente (`PUT /users/{id}`)**
     - Verifica que la respuesta tenga un código de estado 200.
     - Asegúrate de que la respuesta contenga los datos actualizados del usuario, incluyendo `updatedAt`.
     - Valida que los datos actualizados se reflejen correctamente.

   - **Eliminar un usuario (`DELETE /users/{id}`)**
     - Verifica que la respuesta tenga un código de estado 204.
     - Asegúrate de que el usuario se elimine correctamente y no esté presente en futuras solicitudes `GET /users`.

4. **Estructura del archivo de pruebas:**

   Define funciones de prueba para cada operación API. Asegúrate de incluir casos de prueba que cubran:
   - Operaciones básicas.
   - Casos de borde, como la creación de un usuario sin nombre o la actualización de un usuario con datos inválidos.

   Utiliza `assertpy` para realizar aserciones claras y legibles en tus pruebas.

5. **Ejecución de las Pruebas:**

   Utiliza `pytest` para ejecutar tus pruebas. Ejecuta el siguiente comando en tu terminal:

   ```bash
   pytest test_api.py
   ```

6. **Verificación de Resultados:**

   Asegúrate de que todas las pruebas pasen correctamente. Si alguna prueba falla, revisa el código y los mensajes de error para identificar y corregir los problemas.

## Nota sobre `pytest.mark.run`

En esta tarea, utilizamos `pytest.mark.run(order=n)` para especificar el orden en que se ejecutan las pruebas. Esto es útil para asegurar que algunas pruebas, como la creación de un usuario, se ejecuten antes que otras pruebas que dependen de esa creación, como la actualización o eliminación del usuario.

### Ejemplo de Uso de `pytest.mark.run`

```python
@pytest.mark.run(order=1)
def test_get_users():
    # Código de prueba para obtener usuarios

@pytest.mark.run(order=2)
def test_create_user():
    # Código de prueba para crear un usuario

@pytest.mark.run(order=3)
def test_update_user():
    # Código de prueba para actualizar un usuario

@pytest.mark.run(order=4)
def test_delete_user():
    # Código de prueba para eliminar un usuario
```

### Instalación del Plugin `pytest-order`

Para utilizar `pytest.mark.run(order=n)`, necesitas instalar el plugin `pytest-order`. Puedes hacerlo con el siguiente comando:

```bash
pip install pytest-order
```

### Recomendación

Aunque especificar el orden de las pruebas es útil para esta demostración, es recomendable que las pruebas sean independientes entre sí en un entorno real. Esto asegura que un fallo en una prueba no afecte las demás y facilita la localización de errores. Considera usar datos de prueba independientes o reconfigurar el estado del sistema en cada prueba para lograr esto.
