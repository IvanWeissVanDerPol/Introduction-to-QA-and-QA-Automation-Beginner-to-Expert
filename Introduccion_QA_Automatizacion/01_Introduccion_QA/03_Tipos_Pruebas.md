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
- **Herramientas y Frameworks:** NUnit para .NET, JUnit para Java, pytest para Python.
- **Ejemplo:** Probar una función de cálculo de stock en la aplicación de gestión de inventarios para verificar que devuelve el resultado esperado para diferentes entradas.

### Pruebas de Integración

- **Definición:** Verifican la interacción entre diferentes unidades de código.
- **Objetivo:** Asegurar que las unidades integradas funcionen correctamente juntas.
- **Ejemplo:** Probar la interacción entre el módulo de base de datos y la interfaz de usuario de la aplicación de gestión de inventarios para asegurar que los datos de inventario se muestran correctamente en la interfaz.
- **Técnicas de Integración Continua:** Uso de herramientas como Jenkins, Travis CI y GitHub Actions para automatizar la integración y pruebas continuas.

### Pruebas de Sistema

- **Definición:** Verifican el sistema completo para asegurar que cumple con los requisitos.
- **Objetivo:** Validar el sistema completo en un entorno que simule las condiciones de producción.
- **Ejemplo:** Probar toda la aplicación de gestión de inventarios para asegurarse de que todas las funcionalidades, como el seguimiento de inventarios, las alertas de stock bajo y la generación de informes, funcionen como se espera.
- **Pruebas de Extremo a Extremo:** Garantizar que todas las partes del sistema funcionen juntas como se espera desde la entrada del usuario hasta la salida final.

### Pruebas de Aceptación

- **Definición:** Verifican que el sistema cumple con los criterios de aceptación y está listo para su despliegue.
- **Objetivo:** Asegurar que el sistema cumple con las expectativas y necesidades del cliente.
- **Ejemplo:** Realizar pruebas de aceptación del usuario (UAT) para validar que la aplicación de gestión de inventarios cumple con los requisitos del cliente, como la precisión del seguimiento de inventarios y la facilidad de uso de la interfaz.
- **Criterios de Aceptación:** Definición clara de los criterios que el sistema debe cumplir para ser aceptado.

### Pruebas Funcionales

- **Definición:** Verifican que el sistema cumple con los requisitos funcionales especificados.
- **Objetivo:** Validar que las funcionalidades del sistema funcionen como se especifica en los requisitos.
- **Ejemplo:** Probar la funcionalidad de login de la aplicación de gestión de inventarios para verificar que los usuarios puedan iniciar sesión correctamente.
- **Técnicas de Diseño de Casos de Prueba:**
  - **Partición de Equivalencia:** Dividir el dominio de entrada en clases de equivalencia y probar casos representativos.
  - **Análisis de Valores Límite:** Probar los límites de los valores de entrada.

### Pruebas No Funcionales

- **Definición:** Verifican aspectos como rendimiento, seguridad y usabilidad del sistema.
- **Objetivo:** Asegurar que el sistema cumpla con los requisitos no funcionales, tales como tiempos de respuesta, capacidad, y resistencia.
- **Ejemplo:** Realizar pruebas de carga en la aplicación de gestión de inventarios para asegurarse de que el sistema pueda manejar un alto volumen de usuarios simultáneos.

#### Pruebas de Seguridad

- **Herramientas:** OWASP ZAP, Burp Suite.
- **Ejemplo:** Probar la resistencia de la aplicación de gestión de inventarios a ataques de inyección SQL para proteger la base de datos de accesos no autorizados.

#### Pruebas de Rendimiento

- **Herramientas:** JMeter, LoadRunner.
- **Ejemplo:** Evaluar el rendimiento de la aplicación de gestión de inventarios bajo diferentes niveles de carga para asegurar tiempos de respuesta aceptables.

#### Pruebas de Compatibilidad

- **Ejemplo:** Verificar que la aplicación de gestión de inventarios funcione correctamente en diferentes navegadores web, dispositivos móviles y sistemas operativos.

### Otros Tipos de Pruebas

- **Pruebas de Regresión:** Verifican que los cambios recientes no hayan introducido nuevos defectos en el sistema.
  - **Ejemplo:** Después de agregar una nueva funcionalidad de alerta de stock bajo, realizar pruebas de regresión para asegurar que las funcionalidades existentes, como el seguimiento de inventarios, no se vean afectadas.
  
- **Pruebas de Usabilidad:** Evalúan qué tan fácil y agradable es el uso del sistema para los usuarios finales.
  - **Ejemplo:** Realizar pruebas de usabilidad con usuarios finales para identificar posibles mejoras en la interfaz de usuario de la aplicación de gestión de inventarios.

- **Pruebas de Compatibilidad:** Verifican que el sistema funcione en diferentes navegadores, dispositivos y sistemas operativos.
  - **Ejemplo:** Asegurar que la aplicación de gestión de inventarios funcione correctamente en navegadores como Chrome, Firefox y Safari, así como en dispositivos Android e iOS.

- **Pruebas de Humo:** Verifican las funcionalidades críticas del sistema para asegurar que funciona correctamente antes de realizar pruebas más detalladas.
  - **Ejemplo:** Realizar una prueba de humo para verificar que las funciones básicas de la aplicación de gestión de inventarios, como el login y la visualización de inventarios, funcionen correctamente después de una nueva implementación.

- **Pruebas Alfa y Beta:** Pruebas realizadas por usuarios internos (alfa) y un grupo seleccionado de usuarios externos (beta) para detectar errores antes del lanzamiento oficial.
  - **Ejemplo:** En la fase alfa, los empleados de la empresa usan la aplicación de gestión de inventarios internamente para identificar problemas iniciales. En la fase beta, se selecciona un grupo de clientes para probar la aplicación y proporcionar retroalimentación antes del lanzamiento oficial.

