# Casos de Prueba

## Ticket 1: Registro de Usuario

**Requisito:** El formulario de registro debe permitir a los usuarios crear una cuenta proporcionando un nombre de usuario, contraseña, correo electrónico y número de teléfono.

### Caso de Prueba 1.1: Registro de Usuario Exitoso

**Descripción:**
Verificar que un usuario pueda registrarse exitosamente proporcionando todos los campos obligatorios con datos válidos.

**Pasos:**

1. Navegar a la página de registro.
2. Ingresar un nombre de usuario único.
3. Ingresar una contraseña válida que cumpla con los requisitos de seguridad.
4. Ingresar un correo electrónico válido que no esté registrado previamente.
5. Ingresar un número de teléfono válido.
6. Hacer clic en el botón "Registrar".

**Resultado Esperado:**
El usuario debe ser redirigido a una página de confirmación de registro exitoso y recibir un correo electrónico de bienvenida.

## Ticket 2: Inicio de Sesión

**Requisito:** La funcionalidad de inicio de sesión debe permitir a los usuarios acceder a sus cuentas utilizando su nombre de usuario y contraseña.

### Caso de Prueba 2.1: Inicio de Sesión Exitoso

**Descripción:**
Verificar que un usuario pueda iniciar sesión exitosamente con un nombre de usuario y contraseña válidos.

**Pasos:**

1. Navegar a la página de inicio de sesión.
2. Ingresar un nombre de usuario registrado.
3. Ingresar la contraseña correspondiente.
4. Hacer clic en el botón "Iniciar Sesión".

**Resultado Esperado:**
El usuario debe ser redirigido a su panel de cuenta.

## Ticket 3: Restablecimiento de Contraseña

**Requisito:** El sistema debe permitir a los usuarios restablecer su contraseña enviando un enlace de restablecimiento a su correo electrónico registrado.

### Caso de Prueba 3.1: Restablecimiento de Contraseña Exitoso

**Descripción:**
Verificar que un usuario pueda restablecer su contraseña recibiendo un enlace de restablecimiento en su correo electrónico.

**Pasos:**

1. Navegar a la página de inicio de sesión.
2. Hacer clic en el enlace "¿Olvidaste tu contraseña?".
3. Ingresar un correo electrónico registrado.
4. Hacer clic en el botón "Enviar enlace de restablecimiento".
5. Abrir el correo electrónico recibido.
6. Hacer clic en el enlace de restablecimiento proporcionado.
7. Ingresar una nueva contraseña que cumpla con los requisitos de seguridad.
8. Confirmar la nueva contraseña.
9. Hacer clic en el botón "Restablecer contraseña".

**Resultado Esperado:**
El sistema debe mostrar un mensaje de confirmación de restablecimiento exitoso y permitir al usuario iniciar sesión con la nueva contraseña.

## Ticket 4: Agregar Producto al Carrito

**Requisito:** Los usuarios deben poder agregar productos a su carrito de compras desde la página de detalles del producto.

### Caso de Prueba 4.1: Agregar Producto al Carrito Exitoso

**Descripción:**
Verificar que un usuario pueda agregar un producto al carrito desde la página de detalles del producto.

**Pasos:**

1. Navegar a la página de detalles de un producto.
2. Seleccionar las características del producto (tamaño, color, etc.).
3. Hacer clic en el botón "Agregar al carrito".

**Resultado Esperado:**
El sistema debe mostrar un mensaje de confirmación y el producto debe aparecer en el carrito de compras.

## Ticket 5: Finalizar Compra

**Requisito:** El sistema debe permitir a los usuarios finalizar su compra proporcionando detalles de envío y pago.

### Caso de Prueba 5.1: Finalizar Compra Exitosa

**Descripción:**
Verificar que un usuario pueda finalizar su compra proporcionando detalles de envío y pago válidos.

**Pasos:**

1. Navegar al carrito de compras.
2. Hacer clic en el botón "Finalizar compra".
3. Ingresar una dirección de envío válida.
4. Ingresar la información de pago (tarjeta de crédito/débito).
5. Revisar el resumen del pedido.
6. Hacer clic en el botón "Confirmar compra".

**Resultado Esperado:**
El sistema debe mostrar una confirmación de pedido y el usuario debe recibir un correo electrónico de confirmación de compra.

## Ticket 6: Búsqueda de Productos

**Requisito:** La barra de búsqueda debe permitir a los usuarios buscar productos por nombre, categoría o palabra clave.

### Caso de Prueba 6.1: Búsqueda de Producto Exitosa

**Descripción:**
Verificar que un usuario pueda buscar productos utilizando la barra de búsqueda por nombre, categoría o palabra clave.

**Pasos:**

1. Navegar a la página principal.
2. Ingresar un término de búsqueda (nombre, categoría o palabra clave) en la barra de búsqueda.
3. Hacer clic en el icono de búsqueda o presionar Enter.

**Resultado Esperado:**
El sistema debe mostrar una lista de productos relevantes según el término de búsqueda ingresado.

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
