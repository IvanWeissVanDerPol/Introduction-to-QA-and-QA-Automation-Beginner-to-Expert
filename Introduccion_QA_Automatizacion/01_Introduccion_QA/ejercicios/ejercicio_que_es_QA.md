# Tareas: Escritura de Casos de Prueba

## Objetivo

Los alumnos aprenderán a escribir casos de prueba efectivos a partir de tickets de requisitos/funcionalidades específicos. Estos casos de prueba cubrirán diversos tipos de pruebas: unitarias, de integración, de sistema, de aceptación, funcionales, no funcionales, y otros tipos mencionados anteriormente.

## Instrucciones

1. Revisa cada ticket de requisito/funcionalidad proporcionado.
2. Escribe casos de prueba detallados para cada ticket, asegurándote de incluir todos los tipos de pruebas pertinentes.
3. Utiliza el caso de prueba de ejemplo proporcionado como referencia para el formato y el nivel de detalle esperado.

## Ejemplo de Caso de Prueba

### Ticket: Validación del Campo de Contraseña

**Requisito:** El campo de contraseña en el formulario de registro debe aceptar entre 8 y 16 caracteres, incluyendo al menos una letra mayúscula, una letra minúscula, un número y un carácter especial.

### Caso de Prueba: Validación de Contraseña

- **ID del Caso de Prueba:** TC001
- **Descripción:** Verificar que el campo de contraseña acepta y valida correctamente las entradas según las especificaciones.
- **Precondiciones:** El formulario de registro debe estar accesible.
- **Pasos:**
  1. Navegar al formulario de registro.
  2. Ingresar "Pass123!" en el campo de contraseña.
  3. Enviar el formulario.
- **Resultado Esperado:** El sistema debe aceptar la contraseña "Pass123!" como válida.
- **Resultado Real:**
- **Estado:** (Pendiente/Ejecutado)
- **Comentarios:**

## Tickets para Pruebas

### Ticket 1: Registro de Usuario

**Requisito:** El formulario de registro debe permitir a los usuarios crear una cuenta proporcionando un nombre de usuario, contraseña, correo electrónico y número de teléfono.

**Descripción:**
El sistema debe ofrecer un formulario de registro donde los usuarios puedan ingresar sus datos para crear una nueva cuenta. Los campos obligatorios incluyen nombre de usuario, contraseña, correo electrónico y número de teléfono. La contraseña debe tener entre 8 y 16 caracteres, incluyendo al menos una letra mayúscula, una letra minúscula, un número y un carácter especial.

**Criterios de Aceptación:**

1. Todos los campos deben ser obligatorios.
2. La contraseña debe cumplir con los requisitos de seguridad.
3. El sistema debe verificar que el correo electrónico no esté registrado previamente.
4. El formulario debe mostrar mensajes de error claros si algún campo no cumple con los requisitos.

### Ticket 2: Inicio de Sesión

**Requisito:** La funcionalidad de inicio de sesión debe permitir a los usuarios acceder a sus cuentas utilizando su nombre de usuario y contraseña.

**Descripción:**
El sistema debe proporcionar una página de inicio de sesión donde los usuarios puedan ingresar su nombre de usuario y contraseña para acceder a sus cuentas. Debe haber una opción para recuperar la contraseña en caso de olvido.

**Criterios de Aceptación:**

1. El usuario debe poder iniciar sesión con un nombre de usuario y contraseña válidos.
2. El sistema debe mostrar un mensaje de error si las credenciales son incorrectas.
3. Debe haber un enlace para recuperar la contraseña.

### Ticket 3: Restablecimiento de Contraseña

**Requisito:** El sistema debe permitir a los usuarios restablecer su contraseña enviando un enlace de restablecimiento a su correo electrónico registrado.

**Descripción:**
El sistema debe proporcionar una funcionalidad de restablecimiento de contraseña que envíe un enlace de restablecimiento al correo electrónico registrado del usuario. El enlace debe ser válido por un período de tiempo específico.

**Criterios de Aceptación:**

1. El usuario debe recibir un correo electrónico con un enlace de restablecimiento.
2. El enlace de restablecimiento debe expirar después de un tiempo específico.
3. El usuario debe poder ingresar una nueva contraseña que cumpla con los requisitos de seguridad.

### Ticket 4: Agregar Producto al Carrito

**Requisito:** Los usuarios deben poder agregar productos a su carrito de compras desde la página de detalles del producto.

**Descripción:**
En la página de detalles del producto, los usuarios deben tener la opción de seleccionar las características del producto (como tamaño y color) y agregar el producto a su carrito de compras.

**Criterios de Aceptación:**

1. El usuario debe poder seleccionar las características del producto antes de agregarlo al carrito.
2. El sistema debe mostrar una confirmación cuando el producto se haya agregado al carrito.
3. El carrito de compras debe actualizarse para reflejar el nuevo producto.

### Ticket 5: Finalizar Compra

**Requisito:** El sistema debe permitir a los usuarios finalizar su compra proporcionando detalles de envío y pago.

**Descripción:**
El sistema debe guiar a los usuarios a través de un proceso de finalización de compra, donde proporcionen detalles de envío y pago. Al completar la compra, el sistema debe generar una confirmación de pedido.

**Criterios de Aceptación:**

1. El usuario debe ingresar una dirección de envío válida.
2. El sistema debe aceptar y validar la información de pago.
3. El usuario debe recibir una confirmación de pedido después de completar la compra.

### Ticket 6: Búsqueda de Productos

**Requisito:** La barra de búsqueda debe permitir a los usuarios buscar productos por nombre, categoría o palabra clave.

**Descripción:**
El sistema debe proporcionar una barra de búsqueda en la parte superior de la página principal que permita a los usuarios buscar productos por nombre, categoría o palabra clave. Los resultados de la búsqueda deben mostrarse de manera relevante y ordenada.

**Criterios de Aceptación:**

1. El usuario debe poder ingresar texto en la barra de búsqueda.
2. Los resultados deben mostrarse de manera relevante según el término de búsqueda.
3. Los productos deben ser filtrables por categoría y otros atributos relevantes.
