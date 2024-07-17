# Entendiendo APIs RESTful

## Objetivos

- Comprender el concepto y la arquitectura de las APIs RESTful.
- Aprender los diferentes métodos HTTP utilizados en las APIs RESTful.
- Familiarizarse con los formatos de datos comúnmente utilizados en las APIs, como JSON y XML.
- Explorar las herramientas para interactuar y probar APIs RESTful.

## Contenido

### ¿Qué es una API RESTful?

Una API (Interfaz de Programación de Aplicaciones) RESTful es un tipo de API que cumple con los principios del estilo arquitectónico REST (Representational State Transfer). Estas APIs permiten la comunicación entre sistemas mediante solicitudes HTTP para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

### Principios de REST

- **Cliente-Servidor:** La API debe seguir el modelo cliente-servidor.
- **Sin Estado:** Cada solicitud del cliente al servidor debe contener toda la información necesaria para entender y procesar la solicitud.
- **Cacheable:** Las respuestas deben ser explícitamente marcadas como cacheables o no cacheables.
- **Interfaz Uniforme:** Una interfaz uniforme que permita la interacción entre cliente y servidor de manera estándar.
- **Sistema en Capas:** La arquitectura debe estar organizada en capas.

### Métodos HTTP Comunes

- **GET:** Recupera información del servidor.
- **POST:** Envía datos al servidor para crear un nuevo recurso.
- **PUT:** Actualiza un recurso existente en el servidor.
- **DELETE:** Elimina un recurso existente en el servidor.
- **PATCH:** Aplica modificaciones parciales a un recurso.

### Ejemplos de Solicitudes HTTP

- **GET /users:** Recupera una lista de usuarios.
- **POST /users:** Crea un nuevo usuario.
- **PUT /users/1:** Actualiza el usuario con ID 1.
- **DELETE /users/1:** Elimina el usuario con ID 1.
- **PATCH /users/1:** Actualiza parcialmente el usuario con ID 1.

### Formatos de Datos Comunes

Las APIs RESTful generalmente utilizan JSON (JavaScript Object Notation) para la transferencia de datos, aunque también pueden usar XML (eXtensible Markup Language).

#### Ejemplo de JSON

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

#### Ejemplo de XML

```xml
<user>
  <id>1</id>
  <name>John Doe</name>
  <email>john.doe@example.com</email>
</user>
```

### Herramientas para Interactuar y Probar APIs

- **Postman:** Una herramienta popular para probar APIs que permite enviar solicitudes HTTP y ver las respuestas.
- **cURL:** Una herramienta de línea de comandos para transferir datos con URL.
- **Swagger UI:** Una herramienta que permite explorar y probar las APIs directamente desde la documentación.
