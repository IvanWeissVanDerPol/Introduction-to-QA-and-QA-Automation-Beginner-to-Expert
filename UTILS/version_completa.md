
## 01_Introduccion_QA\01_Que_es_QA.md

# ¿Qué es QA?

## Objetivos

- Entender la definición y la importancia de QA.
- Diferenciar entre QA, QC y pruebas.
- Conocer las metodologías de QA como Six Sigma y Total Quality Management (TQM).
- Aprender a implementar QA en diferentes etapas del ciclo de vida del software.
- Entender la implementación de QA en metodologías ágiles y tradicionales.

## Contenido

### Definición de QA

QA (Aseguramiento de la Calidad) es un proceso sistemático de verificar si un producto o servicio cumple con los requisitos especificados y las expectativas del cliente. Se centra en mejorar los procesos de desarrollo y producción para evitar defectos en los productos finales.

### Importancia de QA

- **Prevención de Defectos:** QA se enfoca en prevenir defectos en el proceso de desarrollo y producción en lugar de solo encontrarlos y corregirlos después de que ocurran.
- **Mejora Continua:** Promueve la mejora continua de los procesos y la calidad de los productos.
- **Satisfacción del Cliente:** Garantiza que los productos finales cumplan con las expectativas del cliente y los requisitos establecidos.
- **Eficiencia y Efectividad:** Aumenta la eficiencia y efectividad del proceso de desarrollo, reduciendo costos y tiempos de entrega.

### Diferencia entre QA y QC

- **QA (Aseguramiento de la Calidad):** Enfoque preventivo, orientado a procesos, centrado en la calidad desde el inicio del proceso de desarrollo hasta la entrega final del producto.
  - **Actividades de QA:**
    - Revisión de Requisitos: Asegurar que los requisitos sean claros, completos y verificables.
    - Auditorías de Calidad: Evaluar los procesos y procedimientos para garantizar su adherencia a los estándares de calidad.
    - Capacitación: Formación continua para el equipo de desarrollo sobre las mejores prácticas y estándares de calidad.

- **QC (Control de Calidad):** Enfoque reactivo, orientado a productos, centrado en identificar y corregir defectos en los productos finales.
  - **Actividades de QC:**
    - Pruebas de Software: Verificar que el software funcione según lo especificado.
    - Inspección: Revisar el producto terminado para identificar defectos.
    - Revisiones: Evaluar el producto en diferentes etapas del desarrollo para detectar y corregir errores.

#### Diagramas de Relación entre QA y QC

La imagen a continuación muestra la relación entre Aseguramiento de la Calidad (QA), Control de Calidad (QC) y Pruebas (Testing). QA es un enfoque amplio y preventivo que abarca todas las actividades de mejora de procesos y prevención de defectos. Dentro de QA, el QC es un enfoque más específico y reactivo, centrado en la identificación y corrección de defectos en los productos finales. Finalmente, las pruebas son una actividad específica dentro del QC que implica la ejecución del software para encontrar defectos.

![Diagramas de Relación entre QA y QC](../../Recursos/qa_vs_qc_test.jpg)

### Pruebas vs. QC vs. QA

- **QA (Aseguramiento de la Calidad):** Proceso holístico y proactivo que se centra en mejorar el proceso de desarrollo para prevenir defectos.
- **QC (Control de Calidad):** Parte del QA que se centra en identificar y corregir defectos en los productos finales.
- **Pruebas:** Actividad específica dentro del QC que implica la ejecución del software para encontrar defectos.

### Diferencia entre Pruebas y Depuración

Las pruebas y la depuración son actividades cruciales en el proceso de desarrollo de software, pero tienen objetivos y métodos diferentes:

- **Pruebas (Testing):** Proceso de ejecución de un sistema con la intención de encontrar defectos. Incluye:
  - **Pruebas Dinámicas:** Implican la ejecución del software y observación de su comportamiento. Ejemplos: pruebas funcionales, pruebas de integración.
  - **Pruebas Estáticas:** No requieren la ejecución del software. Ejemplos: revisiones de código, análisis estático.

- **Depuración (Debugging):** Proceso de identificar, analizar y corregir los defectos encontrados durante las pruebas. Incluye:
  - **Localización de Defectos:** Identificar la causa raíz del defecto.
  - **Análisis:** Determinar por qué ocurrió el defecto.
  - **Corrección:** Modificar el código para corregir el defecto.
  - **Verificación:** Asegurarse de que el defecto haya sido corregido y no haya introducido nuevos problemas.

#### Ejemplos Prácticos y Situaciones

- **QA:** Implementación de estándares de codificación y revisión de requisitos.
- **QC:** Ejecución de pruebas automatizadas y revisiones de código.
- **Pruebas:** Pruebas unitarias, de integración y de sistema.
  

## 01_Introduccion_QA\02_Ciclo_Vida_Desarrollo_Software.md

# Ciclo de Vida del Desarrollo de Software (SDLC)

## Objetivos

- Comprender las fases del SDLC.
- Entender el rol de QA en cada fase del SDLC.
- Conocer herramientas y prácticas de cada fase del SDLC.
- Aprender sobre modelos menos conocidos como el modelo espiral y DevOps.
- Entender cómo aplicar QA en metodologías modernas como DevOps.

## Contenido

### Definición del SDLC

El Ciclo de Vida del Desarrollo de Software (SDLC, por sus siglas en inglés) es un proceso estructurado que guía el desarrollo de software a través de varias fases. Proporciona una metodología organizada para la planificación, creación, prueba y despliegue de un sistema de software.

### Fases del SDLC

#### Integración en el Ciclo de Vida del Desarrollo de Software

La imagen a continuación muestra cómo se integra QA en cada fase del ciclo de vida del desarrollo de software (SDLC). Desde la planificación hasta el mantenimiento, QA juega un papel crucial en cada etapa para asegurar la calidad y la satisfacción del cliente.

![Diagramas de QA en SDLC](../../Recursos/sdlcqa.png)

1. **Planificación:**
   - **Objetivo:** Definir los objetivos y el alcance del proyecto.
   - **Actividades:** Análisis de viabilidad, definición de recursos, cronograma y presupuesto.
   - **Entregables:** Plan del proyecto, cronograma, análisis de riesgos.
   - **Rol de QA:** Asegurar que los objetivos sean claros y alcanzables, y que los requisitos de calidad se integren desde el inicio.
   - **Gestión de Riesgos:** QA puede ayudar a identificar y mitigar riesgos a través de la revisión de planes y la evaluación de posibles puntos de falla.
   - **Ejemplo Real:** En un proyecto de desarrollo de una aplicación móvil de gestión de inventarios, la planificación incluiría la estimación de recursos necesarios, la definición de hitos clave y la asignación de tareas específicas al equipo de desarrollo y QA.

2. **Análisis de Requisitos:**
   - **Objetivo:** Recopilar y analizar los requisitos del sistema.
   - **Actividades:** Entrevistas con stakeholders, documentación de requisitos, análisis de viabilidad.
   - **Entregables:** Documentos de requisitos, especificaciones funcionales.
   - **Rol de QA:** Verificar que los requisitos sean completos, claros y verificables, y que contemplen criterios de calidad.
   - **Técnicas:** Entrevistas, talleres de requisitos, análisis de casos de uso.
   - **Ejemplo Real:** Para la aplicación móvil de gestión de inventarios, el análisis de requisitos podría incluir reuniones con los interesados para definir funcionalidades como el seguimiento de inventarios, alertas de stock bajo y generación de informes.

3. **Diseño:**
   - **Objetivo:** Crear la arquitectura y el diseño del sistema.
   - **Actividades:** Diseño de la arquitectura del sistema, diagramas de flujo, diseño de la interfaz de usuario.
   - **Entregables:** Diagramas UML, especificaciones de diseño.
   - **Rol de QA:** Revisar y validar los diseños para asegurar que cumplen con los requisitos y estándares de calidad.
   - **Ejemplos de Artefactos:** Diagramas de clases, diagramas de secuencia.
   - **Ejemplo Real:** En el diseño de la aplicación móvil de gestión de inventarios, se podrían crear diagramas UML para representar las interacciones entre los módulos de seguimiento de inventarios, alertas y generación de informes.

4. **Desarrollo:**
   - **Objetivo:** Codificación y construcción del sistema.
   - **Actividades:** Programación, integración de sistemas, desarrollo de bases de datos.
   - **Entregables:** Código fuente, módulos integrados.
   - **Rol de QA:** Asegurar la adherencia a los estándares de codificación y realizar revisiones de código.
   - **Prácticas Ágiles:** TDD (Test-Driven Development), BDD (Behavior-Driven Development).
   - **Ejemplo Real:** Durante el desarrollo de la aplicación móvil de gestión de inventarios, los desarrolladores escriben código para las funcionalidades de seguimiento de inventarios y generación de informes, mientras QA realiza revisiones de código y pruebas unitarias.

5. **Pruebas:**
   - **Objetivo:** Verificación y validación del sistema.
   - **Actividades:** Pruebas unitarias, pruebas de integración, pruebas de sistema, pruebas de aceptación.
   - **Entregables:** Informes de pruebas, casos de prueba, resultados de pruebas.
   - **Rol de QA:** Planificar, diseñar, ejecutar y reportar las pruebas para asegurar que el sistema cumple con los requisitos y expectativas.
   - **Frameworks de Pruebas:** JUnit, pytest.
   - **Planes de Pruebas:** Crear y gestionar casos de prueba detallados y asegurar su completa ejecución.
   - **Ejemplo Real:** En la aplicación móvil de gestión de inventarios, QA realizaría pruebas de integración para verificar la interacción entre los módulos de seguimiento de inventarios, alertas y generación de informes.

6. **Implementación:**
   - **Objetivo:** Despliegue del sistema en el entorno de producción.
   - **Actividades:** Instalación del sistema, migración de datos, capacitación de usuarios.
   - **Entregables:** Sistema desplegado, usuarios capacitados.
   - **Rol de QA:** Validar el despliegue y realizar pruebas post-implementación para asegurar una transición suave.
   - **Prácticas de Despliegue:** Despliegue continuo, DevOps.
   - **Ejemplo Real:** Para una nueva funcionalidad en la aplicación móvil de gestión de inventarios, QA validaría el despliegue en el entorno de producción y capacitaría a los usuarios en el uso de la nueva funcionalidad.

7. **Mantenimiento:**
   - **Objetivo:** Realización de cambios y mejoras en el sistema.
   - **Actividades:** Corrección de errores, actualizaciones de software, mejoras de funcionalidad.
   - **Entregables:** Actualizaciones, parches, mejoras.
   - **Rol de QA:** Asegurar que los cambios no introduzcan nuevos defectos y que el sistema continúe cumpliendo con los estándares de calidad.
   - **Gestión de Cambios:** Controlar y documentar todos los cambios en el sistema.
   - **Automatización de Pruebas de Regresión:** Asegurar que las nuevas versiones no afecten negativamente las funcionalidades existentes.
   - **Ejemplo Real:** Durante el mantenimiento de la aplicación móvil de gestión de inventarios, QA realizaría pruebas de regresión para asegurar que las actualizaciones del sistema no afecten las funcionalidades existentes, como el seguimiento de inventarios y la generación de informes.

### Modelos del SDLC

Existen varios modelos de SDLC, cada uno con sus propias características y enfoques:

- **Modelo en Cascada:** Proceso secuencial donde cada fase debe completarse antes de que comience la siguiente.
- **Modelo Ágil:** Enfoque flexible y adaptable que promueve entregas incrementales y la colaboración constante con los stakeholders.

### Importancia de QA en el SDLC

QA juega un papel crucial en cada fase del SDLC para asegurar que se cumplan los estándares de calidad y que el producto final cumpla con las expectativas del cliente. QA no es solo responsabilidad del equipo de pruebas, sino que debe integrarse en todo el proceso de desarrollo.


## 01_Introduccion_QA\03_Tipos_Pruebas.md

# Tipos de Pruebas

## Objetivos

- Diferenciar entre los distintos tipos de pruebas.
- Comprender cuándo y cómo se utilizan cada tipo de prueba.
- Conocer herramientas y técnicas específicas para cada tipo de prueba.
- Aprender a diseñar casos de prueba efectivos.

## Contenido

### Pruebas Unitarias

- **Definición:** Verifican el funcionamiento de unidades individuales de código (métodos, funciones, clases).
- **Objetivo:** Asegurar que cada unidad de código funcione correctamente en aislamiento.
- **Ejemplo Real:** Probar una función de cálculo de stock en la aplicación móvil de gestión de inventarios para verificar que devuelve el resultado esperado para diferentes entradas.
  - **Importancia:** Garantiza que las unidades individuales de código funcionan correctamente, lo que facilita la detección y corrección de errores en etapas tempranas del desarrollo.

### Pruebas de Integración

- **Definición:** Verifican la interacción entre diferentes unidades de código.
- **Objetivo:** Asegurar que las unidades integradas funcionen correctamente juntas.
- **Ejemplo Real:** Probar la interacción entre el módulo de base de datos y la interfaz de usuario de la aplicación móvil de gestión de inventarios para asegurar que los datos de inventario se muestran correctamente en la interfaz.
  - **Importancia:** Identifica problemas en la integración de diferentes módulos del sistema, asegurando que las unidades funcionen juntas de manera coherente.

### Pruebas de Sistema

- **Definición:** Verifican el sistema completo para asegurar que cumple con los requisitos.
- **Objetivo:** Validar el sistema completo en un entorno que simule las condiciones de producción.
- **Ejemplo Real:** Probar toda la aplicación móvil de gestión de inventarios para asegurarse de que todas las funcionalidades, como el seguimiento de inventarios, las alertas de stock bajo y la generación de informes, funcionen como se espera.
  - **Importancia:** Garantiza que el sistema completo funcione correctamente y cumpla con los requisitos especificados antes de su despliegue en producción.

### Pruebas de Aceptación

- **Definición:** Verifican que el sistema cumple con los criterios de aceptación y está listo para su despliegue.
- **Objetivo:** Asegurar que el sistema cumple con las expectativas y necesidades del cliente.
- **Ejemplo Real:** Realizar pruebas de aceptación del usuario (UAT) para validar que la aplicación móvil de gestión de inventarios cumple con los requisitos del cliente, como la precisión del seguimiento de inventarios y la facilidad de uso de la interfaz.
  - **Importancia:** Asegura que el sistema cumpla con las expectativas del cliente y esté listo para su uso en el entorno real.

### Pruebas Funcionales

- **Definición:** Verifican que el sistema cumple con los requisitos funcionales especificados.
- **Objetivo:** Validar que las funcionalidades del sistema funcionen como se especifica en los requisitos.
- **Ejemplo Real:** Probar la funcionalidad de login de la aplicación móvil de gestión de inventarios para verificar que los usuarios puedan iniciar sesión correctamente.
  - **Importancia:** Verifica que todas las funcionalidades especificadas se comporten como se espera, garantizando la satisfacción del cliente.

### Pruebas No Funcionales

- **Definición:** Verifican aspectos como rendimiento, seguridad y usabilidad del sistema.
- **Objetivo:** Asegurar que el sistema cumpla con los requisitos no funcionales, tales como tiempos de respuesta, capacidad, y resistencia.
- **Ejemplo Real:** Realizar pruebas de carga en la aplicación móvil de gestión de inventarios para asegurarse de que el sistema pueda manejar un alto volumen de usuarios simultáneos.

#### Pruebas de Seguridad

- **Ejemplo Real:** Probar la resistencia de la aplicación móvil de gestión de inventarios a ataques de inyección SQL para proteger la base de datos de accesos no autorizados.
  - **Importancia:** Garantiza que el sistema es seguro contra vulnerabilidades comunes y protege los datos sensibles de los usuarios.

#### Pruebas de Rendimiento

- **Ejemplo Real:** Evaluar el rendimiento de la aplicación móvil de gestión de inventarios bajo diferentes niveles de carga para asegurar tiempos de respuesta aceptables.
  - **Importancia:** Asegura que el sistema puede manejar la carga esperada y sigue siendo rápido y eficiente bajo condiciones de alta demanda.

### Otros Tipos de Pruebas

- **Pruebas de Regresión:** Verifican que los cambios recientes no hayan introducido nuevos defectos en el sistema.
  - **Ejemplo Real:** Después de agregar una nueva funcionalidad de alerta de stock bajo, realizar pruebas de regresión para asegurar que las funcionalidades existentes, como el seguimiento de inventarios, no se vean afectadas.
  - **Importancia:** Garantiza que nuevas actualizaciones o cambios no afecten negativamente las funcionalidades existentes.

- **Pruebas de Usabilidad:** Evalúan qué tan fácil y agradable es el uso del sistema para los usuarios finales.
  - **Ejemplo Real:** Realizar pruebas de usabilidad con usuarios finales para identificar posibles mejoras en la interfaz de usuario de la aplicación móvil de gestión de inventarios.
  - **Importancia:** Asegura que la aplicación sea intuitiva y fácil de usar, mejorando la satisfacción del usuario final.

- **Pruebas de Compatibilidad:** Verifican que el sistema funcione en diferentes navegadores, dispositivos y sistemas operativos.
  - **Ejemplo Real:** Asegurar que la aplicación móvil de gestión de inventarios funcione correctamente en navegadores como Chrome, Firefox y Safari, así como en dispositivos Android e iOS.
  - **Importancia:** Asegura que todos los usuarios puedan acceder y usar el sistema sin importar su plataforma.

- **Pruebas de Humo:** Verifican las funcionalidades críticas del sistema para asegurar que funciona correctamente antes de realizar pruebas más detalladas.
  - **Ejemplo Real:** Realizar una prueba de humo para verificar que las funciones básicas de la aplicación móvil de gestión de inventarios, como el login y la visualización de inventarios, funcionen correctamente después de una nueva implementación.
  - **Importancia:** Asegura que el sistema está lo suficientemente estable para realizar pruebas más exhaustivas.


## 01_Introduccion_QA\04_Tecnicas_Testing.md

# Técnicas de Testing

## Objetivos

- Comprender las diferentes técnicas de testing.
- Diferenciar entre testing estático y dinámico.
- Conocer las buenas prácticas y habilidades esenciales en testing.
- Aprender sobre el análisis y diseño de pruebas.
- Gestionar las actividades de testing de manera efectiva.

## Contenido

### Testing Estático vs. Dinámico

#### Testing Estático

- **Definición:** El testing estático implica la revisión de artefactos del software sin ejecutar el código.
- **Ejemplos de Actividades de Testing Estático:**
  - **Revisión de código:** Un grupo de desarrolladores revisa el código fuente para identificar errores, mejoras de rendimiento y asegurarse de que se siguen las convenciones de codificación establecidas.
    - **Ejemplo:** En una revisión de código para la aplicación móvil de gestión de inventarios, el equipo podría encontrar un bucle ineficiente que ralentiza la actualización del stock en tiempo real y proponer una optimización.
  - **Inspección:** Un proceso formal y sistemático en el que se examinan documentos de diseño, casos de uso, y especificaciones para encontrar defectos y asegurar la calidad.
    - **Ejemplo:** Inspeccionar el documento de requisitos de la aplicación móvil de gestión de inventarios para asegurarse de que todas las funcionalidades necesarias están claramente especificadas y no hay ambigüedades.
  - **Análisis estático:** Uso de herramientas automatizadas para analizar el código fuente y detectar defectos sin ejecutarlo, como errores de sintaxis, uso de variables no inicializadas, y posibles vulnerabilidades de seguridad.
    - **Ejemplo:** Utilizar SonarQube para analizar el código de la aplicación móvil de gestión de inventarios y detectar problemas como inyecciones de SQL y mal manejo de excepciones.
  - **Revisiones de diseño y arquitectura:** Evaluación detallada de los diseños y la arquitectura del sistema para identificar problemas de diseño que podrían afectar el rendimiento, la escalabilidad, o la mantenibilidad del software.
    - **Ejemplo:** Revisar la arquitectura de la aplicación móvil de gestión de inventarios para asegurarse de que la separación entre el frontend y el backend es clara y que las API están bien definidas y documentadas.
- **Beneficios:**
  - Detección temprana de defectos.
  - Reducción de costos de corrección.
  - Mejora de la calidad del código.

#### Testing Dinámico

- **Definición:** El testing dinámico implica la ejecución del software para verificar su comportamiento.
- **Ejemplos de Actividades de Testing Dinámico:**
  - Pruebas unitarias.
  - Pruebas de integración.
  - Pruebas de sistema.
  - Pruebas de aceptación.
- **Beneficios:**
  - Verificación del comportamiento del software en tiempo de ejecución.
  - Identificación de defectos que solo se manifiestan cuando el software está en funcionamiento.

### Análisis y Diseño de Pruebas

- **Análisis de Pruebas:**
  - Identificar los requisitos y objetivos de las pruebas.
  - Priorizar los casos de prueba basándose en el riesgo y la importancia.
- **Diseño de Pruebas:**
  - Crear casos de prueba detallados que cubran todos los escenarios posibles.
  - Utilizar técnicas de diseño de pruebas como la partición de equivalencia y el análisis de valores límite.
  - **Técnicas de Diseño de Casos de Prueba:**
    - **Partición de Equivalencia:** Dividir el dominio de entrada en clases de equivalencia y probar casos representativos.
      - **Ejemplo:** Para el campo de contraseña, dividir las entradas en clases de equivalencia como contraseñas válidas (correctas), contraseñas inválidas (incorrectas) y campos vacíos. Probar una contraseña correcta, una incorrecta y dejar el campo vacío para asegurarse de que el sistema maneje cada clase adecuadamente.
    - **Análisis de Valores Límite:** Probar los límites de los valores de entrada.
      - **Ejemplo:** Si el campo de contraseña debe tener entre 8 y 16 caracteres, probar con contraseñas de 7, 8, 16 y 17 caracteres para asegurarse de que el sistema acepte y rechace adecuadamente las contraseñas en los límites especificados.
- **Matriz de Trazabilidad de Requisitos:**
  - Asegurar que todos los requisitos estén cubiertos por casos de prueba.
- **Diseño de Prueba Basada en Riesgo:**
  - Enfocar los esfuerzos de prueba en las áreas de mayor riesgo.

### Gestión de las Actividades de Prueba

- **Planificación de Pruebas:**
  - Definir el alcance, los objetivos y los recursos necesarios para las pruebas.
- **Monitoreo y Control de Pruebas:**
  - Seguir el progreso de las pruebas y hacer ajustes según sea necesario.
- **Coordinación de Actividades de Pruebas:**
  - Asegurar una comunicación efectiva entre los miembros del equipo de pruebas.


## 01_Introduccion_QA\ejercicios\ejercicio_que_es_QA.md

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


## 02_Fundamentos_Python\01_Introduccion_Python.md

# Introducción a Python

## Objetivos

- Entender la sintaxis básica y cómo ejecutar programas en Python.

## Contenido

### Características de Python

- **Fácil de Leer y Escribir:** Python tiene una sintaxis sencilla y clara.
- **Interpretado:** No necesita compilación, se ejecuta directamente del código fuente.
- **Tipado Dinámico:** No es necesario declarar tipos de variables.
- **Multiplataforma:** Funciona en diversos sistemas operativos.
- **Gran Comunidad y Bibliotecas:** Amplio soporte y una gran cantidad de bibliotecas y módulos disponibles.

### Instalación de Python

Para instalar Python, puedes descargarlo desde [python.org](https://www.python.org/downloads/) y seguir las instrucciones de instalación para tu sistema operativo.

### Ejecución de Programas en Python

Puedes escribir y ejecutar programas de Python utilizando un entorno de desarrollo integrado (IDE) como PyCharm, VSCode, o simplemente usando un editor de texto y ejecutando los scripts desde la línea de comandos.

### Sintaxis Básica

- **Comentarios:** Se utilizan el símbolo `#` para comentarios de una sola línea y `''' ... '''` o `""" ... """` para comentarios de múltiples líneas.

```python
  # Esto es un comentario de una sola línea
  
  """
  Esto es un comentario
  de múltiples líneas
  """
```

**Variables y Tipos de Datos:**

```Python
nombre = "Juan"  # Cadena de texto
edad = 25        # Entero
altura = 1.75    # Flotante
es_estudiante = True  # Booleano
```

**Estructuras de Control:**

```Python
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

**Bucles**:

```Python
for i in range(5):
    print(i)

while edad < 30:
    print("Aún eres joven")
    edad += 1
```


## 02_Fundamentos_Python\02_Funciones_Modulos.md

# Funciones y Módulos en Python

## Objetivos

- Entender cómo definir y llamar funciones en Python.
- Aprender a importar y utilizar módulos.
- Introducir los conceptos básicos de Programación Orientada a Objetos (OOP) en Python.

## Contenido

### Funciones en Python

Las funciones son bloques de código reutilizables que realizan una tarea específica. Se definen utilizando la palabra clave `def`.

#### Definición de Funciones

```Python
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")
```

#### Parámetros y Argumentos

```Python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)  # Output: 8
```

#### Funciones con Valores Predeterminados

```Python
def saludar(nombre="amigo"):
    print(f"Hola, {nombre}!")

saludar()  # Output: Hola, amigo!
saludar("Ana")  # Output: Hola, Ana!
```

### Módulos en Python

Un módulo es un archivo que contiene definiciones y declaraciones de Python. Se puede importar un módulo completo o partes específicas de él.

#### Importar Módulos

```Python
import math

print(math.sqrt(16))  # Output: 4.0
```

#### Importar Funciones Específicas de un Módulo

```Python
from math import sqrt

print(sqrt(25))  # Output: 5.0
```

#### Crear y Usar Módulos Propios

Crea un archivo mimodulo.py:

```Python
def saludar(nombre):
    print(f"Hola, {nombre}!")
```

Importa y usa tu módulo:

```Python
import mimodulo

mimodulo.saludar("María")  # Output: Hola, María!
```

### Programación Orientada a Objetos (OOP) en Python

La Programación Orientada a Objetos (OOP) es un paradigma de programación que utiliza "objetos" y "clases". Una clase es como un plano para crear objetos. Un objeto es una instancia de una clase.

### Definición de una Clase

```Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de la clase Persona
juan = Persona("Juan", 30)
juan.saludar()  # Output: Hola, mi nombre es Juan y tengo 30 años.
```

### Atributos y Métodos

Los atributos son variables que pertenecen a una clase. Los métodos son funciones que pertenecen a una clase.

```Python
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"La velocidad del {self.marca} {self.modelo} es {self.velocidad} km/h.")

    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"La velocidad del {self.marca} {self.modelo} es {self.velocidad} km/h.")

# Crear una instancia de la clase Coche
mi_coche = Coche("Toyota", "Corolla")
mi_coche.acelerar(50)  # Output: La velocidad del Toyota Corolla es 50 km/h.
mi_coche.frenar(20)    # Output: La velocidad del Toyota Corolla es 30 km/h.
```

### Herencia

La herencia permite crear una nueva clase que es una modificación de una clase existente.

```Python
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        print(f"Este es un {self.marca} {self.modelo}.")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def descripcion(self):
        super().descripcion()
        print(f"Es una moto de tipo {self.tipo}.")

# Crear una instancia de la clase Moto
mi_moto = Moto("Honda", "CBR", "Deportiva")
mi_moto.descripcion()
# Output:
# Este es un Honda CBR.
# Es una moto de tipo Deportiva.
```

### Encapsulamiento

El encapsulamiento se refiere a la restricción del acceso a algunos de los componentes de un objeto.

```Python
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print(f"El saldo de {self.titular} es {self.__saldo}.")

# Crear una instancia de la clase CuentaBancaria
cuenta = CuentaBancaria("Ana", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.mostrar_saldo()  # Output: El saldo de Ana es 1300.
```


## 02_Fundamentos_Python\03_Manipulacion_Datos.md

# Manipulación de Datos en Python

## Objetivos

- Conocer las estructuras de datos básicas en Python.
- Aprender a manipular listas, tuplas, diccionarios y conjuntos.

## Contenido

### Listas

Las listas son colecciones ordenadas y mutables que permiten almacenar múltiples elementos. Las listas en Python pueden contener diferentes tipos de datos, incluidos otros objetos de listas.

#### Crear y Acceder a Listas

```python
frutas = ["manzana", "banana", "cereza"]

print(frutas[0])  # Output: manzana
```

#### Operaciones con Listas

```python
    frutas.append("naranja")
    print(frutas)  # Output: ["manzana", "banana", "cereza", "naranja"]

    frutas.remove("banana")
    print(frutas)  # Output: ["manzana", "cereza", "naranja"]

    print(len(frutas))  # Output: 3
```

### Tuplas

Las tuplas son colecciones ordenadas e inmutables.

#### Crear y Acceder a Tuplas

```python
    numeros = (1, 2, 3, 4)
    print(numeros[1])  # Output: 2
```

### Diccionarios

Los diccionarios son colecciones no ordenadas de pares clave-valor.

#### Crear y Acceder a Diccionarios

```python
    estudiante = {"nombre": "Juan", "edad": 25, "carrera": "Ingeniería"}
    print(estudiante["nombre"])  # Output: Juan
```

#### Operaciones con Diccionarios

```python
    estudiante["edad"] = 26
    print(estudiante)  # Output: {"nombre": "Juan", "edad": 26, "carrera": "Ingeniería"}

    estudiante["universidad"] = "MIT"
    print(estudiante)  # Output: {"nombre": "Juan", "edad": 26, "carrera": "Ingeniería", "universidad": "MIT"}

    del estudiante["carrera"]
    print(estudiante)  # Output: {"nombre": "Juan", "edad": 26, "universidad": "MIT"}
```

### Conjuntos

Los conjuntos son colecciones desordenadas de elementos únicos.

#### Crear y Operar con Conjuntos

```python
    frutas = {"manzana", "banana", "cereza"}
    frutas.add("naranja")
    print(frutas)  # Output: {"manzana", "banana", "cereza", "naranja"}

    frutas.remove("banana")
    print(frutas)  # Output: {"manzana", "cereza", "naranja"}
```

### Comentarios Adicionales

1. **Listas:**
   - Las listas son muy versátiles y pueden contener elementos de diferentes tipos de datos.
   - Son útiles para almacenar colecciones de elementos que pueden cambiar de tamaño.

2. **Tuplas:**
   - Las tuplas, al ser inmutables, son más rápidas que las listas y pueden ser utilizadas como claves en un diccionario.
   - Son útiles cuando se necesita un conjunto de datos constante.

3. **Diccionarios:**
   - Los diccionarios son extremadamente útiles para representar datos estructurados (como objetos) y para búsquedas rápidas.
   - Cada clave en un diccionario debe ser única.

4. **Conjuntos:**
   - Los conjuntos eliminan automáticamente los elementos duplicados.
   - Son útiles para operaciones matemáticas como intersección, unión y diferencia de conjuntos.


## 02_Fundamentos_Python\ejercicios\ejercicio_fundamentos_python.md

# Tarea: Crear un Módulo de Calculadora

## Objetivo

Crear un módulo de Python para una calculadora utilizando Programación Orientada a Objetos (OOP) que incluya todas las operaciones matemáticas básicas. Luego, crear un archivo principal separado para importar y usar el módulo de la calculadora. Este módulo se utilizará más adelante para las tareas de pruebas en otra sección del curso.

## Parte 1: Módulo de Calculadora

### Paso 1: Crear el Módulo de Calculadora

1. Crear un archivo llamado `calculadora.py`.
2. Este archivo contendrá una clase `Calculadora` con métodos para cada operación matemática.
3. Implementar los siguientes métodos en la clase `Calculadora`:
   - Suma
   - Resta
   - Multiplicación
   - División
   - Módulo
   - Exponenciación
   - División Entera
4. Asegurarse de que cada método:
   - Tome dos entradas numéricas.
   - Devuelva el resultado de la operación.
   - Maneje adecuadamente casos especiales, como la división por cero.

### Paso 2: Crear el Archivo Principal

1. Crear un archivo llamado `main.py`.
2. Este archivo importará y usará la clase `Calculadora` de `calculadora.py`.
3. Implementar lo siguiente en `main.py`:
   - Importar la clase `Calculadora`.
   - Crear una instancia de la clase `Calculadora`.
   - Realizar algunos cálculos utilizando los métodos de la clase `Calculadora`.
   - Imprimir los resultados de los cálculos.

### Paso 3: Probar la Calculadora

1. Ejecutar `main.py`.
2. Asegurarse de que todas las operaciones estén correctamente implementadas y muestren los resultados esperados.

### Ejemplo de Salida

```terminal
Operaciones de Calculadora
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0
10 % 5 = 0
10 ** 5 = 100000
10 // 5 = 2
```


## 03_Pruebas_Automatizadas\01_Introduccion_Pruebas_Automatizadas.md

# Introducción a las Pruebas Automatizadas

## Objetivos

- Entender el concepto de pruebas automatizadas y su importancia.
- Conocer las ventajas y desafíos de la automatización de pruebas.

## Contenido

### ¿Qué son las Pruebas Automatizadas?

Las pruebas automatizadas son el uso de herramientas de software para ejecutar pruebas predefinidas en una aplicación, comparar los resultados reales con los resultados esperados y generar informes sobre el éxito o fracaso de estas pruebas.

### Importancia de las Pruebas Automatizadas

- **Eficiencia:** Las pruebas automatizadas pueden ejecutarse rápidamente y repetirse fácilmente, lo que ahorra tiempo y recursos en comparación con las pruebas manuales.
- **Cobertura:** Permiten una mayor cobertura de pruebas, ya que pueden ejecutar una gran cantidad de casos de prueba en menos tiempo.
- **Consistencia:** Eliminan la variabilidad humana, asegurando que las pruebas se ejecuten de la misma manera cada vez.
- **Regresión:** Facilitan la ejecución de pruebas de regresión para detectar errores introducidos por cambios recientes en el código.

### Ventajas de las Pruebas Automatizadas

- **Rapidez:** Las pruebas automatizadas se pueden ejecutar mucho más rápido que las pruebas manuales.
- **Repetibilidad:** Las pruebas pueden repetirse tantas veces como sea necesario sin intervención humana.
- **Escalabilidad:** Es posible ejecutar un gran número de pruebas en paralelo.
- **Documentación:** Las pruebas automatizadas sirven como documentación viva del comportamiento esperado del sistema.

### Desafíos de las Pruebas Automatizadas

- **Costo Inicial:** La configuración y el desarrollo de scripts de prueba automatizados pueden requerir una inversión significativa de tiempo y recursos.
- **Mantenimiento:** Los scripts de prueba deben mantenerse actualizados con los cambios en la aplicación.
- **Conocimiento Técnico:** Requiere habilidades técnicas para escribir y mantener scripts de prueba.

### Herramientas de Pruebas Automatizadas

Existen muchas herramientas disponibles para la automatización de pruebas, algunas de las más populares incluyen:

- **Selenium:** Para la automatización de pruebas de aplicaciones web.
- **PyTest:** Para pruebas unitarias en Python.
- **Cucumber:** Para pruebas basadas en comportamiento (BDD).


## 03_Pruebas_Automatizadas\02_Escribiendo_Scripts_Prueba.md

# Escribiendo Scripts de Prueba

## Objetivos

- Aprender a escribir scripts de prueba automatizados.
- Conocer las mejores prácticas para la creación de scripts de prueba.

## Contenido

### ¿Qué es un Script de Prueba?

Un script de prueba es un conjunto de instrucciones que se ejecutan de manera automatizada para validar el comportamiento de una aplicación. Estos scripts están diseñados para simular acciones del usuario y verificar que el sistema responda como se espera.

### Estructura de un Script de Prueba

1. **Configuración:** Preparar el entorno de prueba y los datos necesarios.
2. **Ejecución:** Realizar las acciones necesarias para la prueba.
3. **Verificación:** Comprobar que los resultados son los esperados.
4. **Limpieza:** Dejar el sistema en un estado limpio después de la prueba.

### Ejemplo de Script de Prueba Simple con `pytest` (Python)

```python
import pytest
from calculator import Calculadora

@pytest.fixture
def calculadora():
    return Calculadora()

def test_sumar(calculadora):
    # Casos de prueba básicos
    assert calculadora.sumar(10, 5) == 15
    assert calculadora.sumar(-1, 1) == 0
    assert calculadora.sumar(-1, -1) == -2
    
    # Casos de prueba adicionales
    assert calculadora.sumar(0, 0) == 0
    assert calculadora.sumar(1000, 2000) == 3000
    assert calculadora.sumar(-1000, -2000) == -3000
    assert calculadora.sumar(1.5, 2.5) == 4.0
    assert calculadora.sumar(-1.5, 1.5) == 0.0

```


## 03_Pruebas_Automatizadas\03_Pruebas_Unitarias.md

# Pruebas Unitarias

## Objetivos

- Entender el concepto y la importancia de las pruebas unitarias.
- Aprender a escribir y ejecutar pruebas unitarias en Python.

## Contenido

### ¿Qué son las Pruebas Unitarias?

Las pruebas unitarias son un tipo de prueba de software que verifica el funcionamiento de componentes individuales del código, como funciones o métodos. Su objetivo es asegurar que cada unidad de código funcione correctamente de manera aislada.

### Importancia de las Pruebas Unitarias

- **Detección Temprana de Errores:** Permiten identificar errores en etapas tempranas del desarrollo.
- **Facilitan el Refactorizado:** Aseguran que el código sigue funcionando correctamente después de realizar cambios.
- **Documentación:** Proveen una documentación adicional del comportamiento esperado del código.
- **Mejoran la Calidad del Código:** Fomentan el desarrollo de código modular y bien diseñado.

### Herramientas para Pruebas Unitarias en Python

- **unittest:** Módulo estándar de Python para escribir y ejecutar pruebas unitarias.
- **pytest:** Framework de pruebas más avanzado que soporta fixtures, plugins y es compatible con unittest.

### Escribiendo Pruebas Unitarias con unittest

```python
# test_calculadora_unittest.py
import unittest
from calculator import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        # Configuración: Crear una instancia de la calculadora
        self.calc = Calculadora()

    def test_sumar(self):
        # Ejecución: Realizar la operación de suma
        resultado = self.calc.sumar(10, 5)
        # Verificación: Comprobar que el resultado es el esperado
        self.assertEqual(resultado, 15)

    def tearDown(self):
        # Limpieza: Aquí podrías limpiar datos si fuera necesario
        pass

if __name__ == "__main__":
    unittest.main()

```

### Escribiendo Pruebas Unitarias con pytest

```python
# test_calculadora_pytest.py
import pytest
from calculator import Calculadora

@pytest.fixture
def calculadora():
    return Calculadora()

def test_sumar(calculadora):
    # Casos de prueba básicos
    assert calculadora.sumar(10, 5) == 15
    assert calculadora.sumar(-1, 1) == 0
    assert calculadora.sumar(-1, -1) == -2
    
    # Casos de prueba adicionales
    assert calculadora.sumar(0, 0) == 0
    assert calculadora.sumar(1000, 2000) == 3000
    assert calculadora.sumar(-1000, -2000) == -3000
    assert calculadora.sumar(1.5, 2.5) == 4.0
    assert calculadora.sumar(-1.5, 1.5) == 0.0

# Para ejecutar las pruebas, usa el comando:
# pytest test_calculadora_pytest.py

```

### Mejores Prácticas para Pruebas Unitarias

- Aislamiento: Las pruebas deben ser independientes y no depender de otras pruebas.
- Cobertura: Asegurar que se prueban todos los casos posibles, incluyendo bordes y errores.
- Nomenclatura: Utilizar nombres descriptivos para las pruebas y los métodos de prueba.
- Automatización: Integrar las pruebas en el proceso de integración continua para ejecutarlas automáticamente en cada cambio de código.


## 03_Pruebas_Automatizadas\ejercicios\ejercicio_pruebas_automatizadas.md

# Desarrollo de Pruebas Unitarias con pytest para Calculadora

## Objetivo

Desarrollar pruebas unitarias utilizando pytest para verificar todas las funciones de la calculadora creada previamente. Las pruebas deben asegurar que cada operación matemática se realiza correctamente y manejar casos de borde como la división por cero.

## Instrucciones

### Preparar el entorno de pruebas

Asegúrate de tener pytest instalado en tu entorno. Puedes instalarlo usando el siguiente comando:

```bash
pip install pytest
```

### Crear el archivo de pruebas

Crea un archivo llamado `test_calculadora.py` en el mismo directorio donde se encuentra tu módulo `calculator.py`.

### Implementar las pruebas

Escribe pruebas unitarias para cada función de tu clase `Calculadora` en `calculator.py`. Asegúrate de probar los siguientes métodos:

- sumar
- restar
- multiplicar
- dividir
- modulo
- exponenciar
- dividir_piso

### Estructura del archivo de pruebas

1. Define una fixture para inicializar una instancia de la calculadora.
2. Escribe una función de prueba para cada operación matemática.
3. Asegúrate de incluir casos de prueba que cubran:
   - Operaciones básicas con números positivos y negativos.
   - Casos de borde, como la división por cero.


## 04_APIs_RESTful\01_Entendiendo_APIs_RESTful.md

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


## 04_APIs_RESTful\02_Automatizando_Pruebas_API.md

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


## 04_APIs_RESTful\ejercicios\ejercicio_apis_restful.md

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


## 05_Selenium_Basico\01_Introduccion_Selenium.md



## 05_Selenium_Basico\02_Configuracion_Selenium.md



## 05_Selenium_Basico\03_Escribiendo_Scripts_Selenium.md



## 05_Selenium_Basico\04_Interacciones_Formularios.md



## 05_Selenium_Basico\05_Manejo_Popups_Alertas.md



## 05_Selenium_Basico\ejercicios\ejercicio_selenium_basico.md


