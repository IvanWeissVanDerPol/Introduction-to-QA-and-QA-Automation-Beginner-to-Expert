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
