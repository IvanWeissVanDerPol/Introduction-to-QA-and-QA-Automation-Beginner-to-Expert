# Automatizando Pruebas API con Python

## Objetivos

- Aprender a realizar solicitudes HTTP utilizando Python `requests`.
- Conocer cómo trabajar con respuestas JSON.
- Implementar aserciones fluidas utilizando `assertpy` para validar respuestas.
- Integrar y automatizar pruebas API en su framework.

## Contenido

### Realizando Solicitudes HTTP con Python `requests`

Las solicitudes HTTP son la base para interactuar con APIs RESTful. Python ofrece la librería `requests` para facilitar esta tarea.

#### Instalación de `requests`

```bash
pip install requests
```

#### Ejemplos de Solicitudes HTTP

##### GET Request

```python
import requests

response = requests.get('https://reqres.in/api/users?page=2')
print(response.status_code)  # Output: 200
print(response.json())  # Output: JSON response content
```

##### POST Request

```python
data = {
    "name": "John",
    "job": "developer"
}

response = requests.post('https://reqres.in/api/users', json=data)
print(response.status_code)  # Output: 201
print(response.json())  # Output: JSON response content with created user details
```

##### PUT Request

```python
data = {
    "name": "John",
    "job": "manager"
}

response = requests.put('https://reqres.in/api/users/2', json=data)
print(response.status_code)  # Output: 200
print(response.json())  # Output: JSON response content with updated user details
```

##### DELETE Request

```python
response = requests.delete('https://reqres.in/api/users/2')
print(response.status_code)  # Output: 204
```

### Trabajando con Respuestas JSON

Las respuestas de las APIs suelen estar en formato JSON. Aquí se muestra cómo trabajar con ellas.

```python
response = requests.get('https://reqres.in/api/users?page=2')
data = response.json()
print(data['data'])  # Accessing specific fields in the JSON response
```

### Utilizando `assertpy` para Aserciones Fluidas

`assertpy` es una librería de aserciones que permite realizar validaciones de manera más legible y fluida.

#### Instalación de `assertpy`

```bash
pip install assertpy
```

#### Ejemplos de Aserciones Fluidas

```python
from assertpy import assert_that

response = requests.get('https://reqres.in/api/users?page=2')
json_data = response.json()

assert_that(response.status_code).is_equal_to(200)
assert_that(json_data['page']).is_equal_to(2)
assert_that(json_data['data']).is_type_of(list)
assert_that(json_data['data']).is_not_empty()
assert_that(json_data['data'][0]).contains_key('id').contains_key('email')
```

### Ejemplo Completo: Automatización de Pruebas API

Combina todo lo aprendido para automatizar una serie de pruebas API.

```python
import requests
from assertpy import assert_that

def test_get_users():
    response = requests.get('https://reqres.in/api/users?page=2')
    json_data = response.json()

    assert_that(response.status_code).is_equal_to(200)
    assert_that(json_data['page']).is_equal_to(2)
    assert_that(json_data['data']).is_type_of(list)
    assert_that(json_data['data']).is_not_empty()
    assert_that(json_data['data'][0]).contains_key('id').contains_key('email')

def test_create_user():
    data = {"name": "John", "job": "developer"}
    response = requests.post('https://reqres.in/api/users', json=data)
    json_data = response.json()

    assert_that(response.status_code).is_equal_to(201)
    assert_that(json_data).contains_key('id').contains_key('createdAt')

def test_update_user():
    data = {"name": "John", "job": "manager"}
    response = requests.put('https://reqres.in/api/users/2', json=data)
    json_data = response.json()

    assert_that(response.status_code).is_equal_to(200)
    assert_that(json_data).contains_entry({'name': 'John', 'job': 'manager'}).contains_key('updatedAt')

def test_delete_user():
    response = requests.delete('https://reqres.in/api/users/2')
    assert_that(response.status_code).is_equal_to(204)
```
