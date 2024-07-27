# Casos de Prueba

## Ticket 1: Registro de Usuario

**Requisito:** El formulario de registro debe permitir a los usuarios crear una cuenta proporcionando un nombre de usuario, contraseña, correo electrónico y número de teléfono.

### Caso de Prueba 1.1: Registro de Usuario Exitoso

**Descripción:**
Verificar que un usuario pueda registrarse exitosamente proporcionando todos los campos obligatorios con datos válidos.

**Pasos:**

1. Navegar a la página de registro.
	* **Resultado del Paso:** La página de registro se carga correctamente.
2. Ingresar un nombre de usuario único.
	* **Resultado del Paso:** El nombre de usuario se ingresa correctamente.
3. Ingresar una contraseña válida que cumpla con los requisitos de seguridad.
	* **Resultado del Paso:** La contraseña se ingresa correctamente.
4. Ingresar un correo electrónico válido que no esté registrado previamente.
	* **Resultado del Paso:** El correo electrónico se ingresa correctamente.
5. Ingresar un número de teléfono válido.
	* **Resultado del Paso:** El número de teléfono se ingresa correctamente.
6. Hacer clic en el botón "Registrar".
	* **Resultado del Paso:** El formulario de registro se envía correctamente.

**Resultado Esperado:**
El usuario debe ser redirigido a una página de confirmación de registro exitoso y recibir un correo electrónico de bienvenida.

**Resultado Actual:**
El usuario es redirigido a una página de confirmación de registro exitoso y recibe un correo electrónico de bienvenida.

## Ticket 2: Inicio de Sesión

**Requisito:** La funcionalidad de inicio de sesión debe permitir a los usuarios acceder a sus cuentas utilizando su nombre de usuario y contraseña.

### Caso de Prueba 2.1: Inicio de Sesión Exitoso

**Descripción:**
Verificar que un usuario pueda iniciar sesión exitosamente con un nombre de usuario y contraseña válidos.

**Pasos:**

1. Navegar a la página de inicio de sesión.
	* **Resultado del Paso:** La página de inicio de sesión se carga correctamente.
2. Ingresar un nombre de usuario registrado.
	* **Resultado del Paso:** El nombre de usuario se ingresa correctamente.
3. Ingresar la contraseña correspondiente.
	* **Resultado del Paso:** La contraseña se ingresa correctamente.
4. Hacer clic en el botón "Iniciar Sesión".
	* **Resultado del Paso:** El formulario de inicio de sesión se envía correctamente.

**Resultado Esperado:**
El usuario debe ser redirigido a su panel de cuenta.

**Resultado Actual:**
El usuario es redirigido a su panel de cuenta.

## Ticket 3: Restablecimiento de Contraseña

**Requisito:** El sistema debe permitir a los usuarios restablecer su contraseña enviando un enlace de restablecimiento a su correo electrónico registrado.

### Caso de Prueba 3.1: Restablecimiento de Contraseña Exitoso

**Descripción:**
Verificar que un usuario pueda restablecer su contraseña recibiendo un enlace de restablecimiento en su correo electrónico.

**Pasos:**

1. Navegar a la página de inicio de sesión.
	* **Resultado del Paso:** La página de inicio de sesión se carga correctamente.
2. Hacer clic en el enlace "¿Olvidaste tu contraseña?".
	* **Resultado del Paso:** La página de restablecimiento de contraseña se carga correctamente.
3. Ingresar un correo electrónico registrado.
	* **Resultado del Paso:** El correo electrónico se ingresa correctamente.
4. Hacer clic en el botón "Enviar enlace de restablecimiento".
	* **Resultado del Paso:** El enlace de restablecimiento se envía correctamente.
5. Abrir el correo electrónico recibido.
	* **Resultado del Paso:** El correo electrónico de restablecimiento se recibe correctamente.
6. Hacer clic en el enlace de restablecimiento proporcionado.
	* **Resultado del Paso:** La página de restablecimiento de contraseña se carga correctamente.
7. Ingresar una nueva contraseña que cumpla con los requisitos de seguridad.
	* **Resultado del Paso:** La nueva contraseña se ingresa correctamente.
8. Confirmar la nueva contraseña.
	* **Resultado del Paso:** La confirmación de la contraseña se ingresa correctamente.
9. Hacer clic en el botón "Restablecer contraseña".
	* **Resultado del Paso:** La contraseña se restablece correctamente.

**Resultado Esperado:**
El sistema debe mostrar un mensaje de confirmación de restablecimiento exitoso y permitir al usuario iniciar sesión con la nueva contraseña.

**Resultado Actual:**
El sistema muestra un mensaje de confirmación de restablecimiento exitoso y permite al usuario iniciar sesión con la nueva contraseña.

## Ticket 4: Agregar Producto al Carrito

**Requisito:** Los usuarios deben poder agregar productos a su carrito de compras desde la página de detalles del producto.

### Caso de Prueba 4.1: Agregar Producto al Carrito Exitoso

**Descripción:**
Verificar que un usuario pueda agregar un producto al carrito desde la página de detalles del producto.

**Pasos:**

1. Navegar a la página de detalles de un producto.
	* **Resultado del Paso:** La página de detalles del producto se carga correctamente.
2. Seleccionar las características del producto (tamaño, color, etc.).
	* **Resultado del Paso:** Las características del producto se seleccionan correctamente.
3. Hacer clic en el botón "Agregar al carrito".
	* **Resultado del Paso:** El producto se agrega al carrito correctamente.

**Resultado Esperado:**
El sistema debe mostrar un mensaje de confirmación y el producto debe aparecer en el carrito de compras.

**Resultado Actual:**
El sistema muestra un mensaje de confirmación y el producto aparece en el carrito de compras.

## Ticket 5: Finalizar Compra

**Requisito:** El sistema debe permitir a los usuarios finalizar su compra proporcionando detalles de envío y pago.

### Caso de Prueba 5.1: Finalizar Compra Exitosa

**Descripción:**
Verificar que un usuario pueda finalizar su compra proporcionando detalles de envío y pago válidos.

**Pasos:**

1. Navegar al carrito de compras.
	* **Resultado del Paso:** El carrito de compras se carga correctamente.
2. Hacer clic en el botón "Finalizar compra".
	* **Resultado del Paso:** La página de finalización de compra se carga correctamente.
3. Ingresar una dirección de envío válida.
	* **Resultado del Paso:** La dirección de envío se ingresa correctamente.
4. Ingresar la información de pago (tarjeta de crédito/débito).
	* **Resultado del Paso:** La información de pago se ingresa correctamente.
5. Revisar el resumen del pedido.
	* **Resultado del Paso:** El resumen del pedido se muestra correctamente.
6. Hacer clic en el botón "Confirmar compra".
	* **Resultado del Paso:** La compra se confirma correctamente.

**Resultado Esperado:**
El sistema debe mostrar una confirmación de pedido y el usuario debe recibir un correo electrónico de confirmación de compra.

**Resultado Actual:**
El sistema muestra una confirmación de pedido y el usuario recibe un correo electrónico de confirmación de compra.

## Ticket 6: Búsqueda de Productos

**Requisito:** La barra de búsqueda debe permitir a los usuarios buscar productos por nombre, categoría o palabra clave.

### Caso de Prueba 6.1: Búsqueda de Producto Exitosa

**Descripción:**
Verificar que un usuario pueda buscar productos utilizando la barra de búsqueda por nombre, categoría o palabra clave.

**Pasos:**

1. Navegar a la página principal.
	* **Resultado del Paso:** La página principal se carga correctamente.
2. Ingresar un término de búsqueda (nombre, categoría o palabra clave) en la barra de búsqueda.
	* **Resultado del Paso:** El término de búsqueda se ingresa correctamente.
3. Hacer clic en el icono de búsqueda o presionar Enter.
	* **Resultado del Paso:** Los resultados de la búsqueda se cargan correctamente.

**Resultado Esperado:**
El sistema debe mostrar una lista de productos relevantes según el término de búsqueda ingresado.

**Resultado Actual:**
El sistema muestra una lista de productos relevantes según el término de búsqueda ingresado.

## Inspiración para Casos de Prueba

- Registro de Usuario con Campos Incompletos
- Inicio de Sesión con Credenciales Incorrectas
- Restablecimiento de Contraseña con Correo No Registrado
- Agregar Producto al Carrito con Diferentes Variantes
- Finalizar Compra con Información de Pago Inválida
- Búsqueda de Productos con Términos Genéricos y Específicos
- Verificación de Mensajes de Error en el Registro de Usuario
- Inicio de Sesión Después de Restablecer la Contraseña
- Eliminar Producto del Carrito de Compras
- Actualizar Cantidad de Productos en el Carrito
- Finalizar Compra con Dirección de Envío Internacional
- Filtrar Resultados de Búsqueda por Categoría
