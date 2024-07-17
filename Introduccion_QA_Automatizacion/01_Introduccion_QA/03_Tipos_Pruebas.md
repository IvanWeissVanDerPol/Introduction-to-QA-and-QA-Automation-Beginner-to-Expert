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
