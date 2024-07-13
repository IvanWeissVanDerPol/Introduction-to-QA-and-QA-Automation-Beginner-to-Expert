# Ejercicio: ¿Qué es QA?

## Descripción
Realiza una búsqueda en internet sobre las diferencias entre QA (Aseguramiento de la Calidad) y QC (Control de Calidad).

## Tareas

### Diferencias entre QA y QC
1. Lee el contenido sobre QA y realiza una búsqueda sobre las diferencias entre QA y QC.

### Fase del SDLC y Rol de QA
1. Investiga más sobre cada fase del SDLC y cómo QA interviene en cada una de ellas.
2. Elabora un diagrama que represente el SDLC y el rol de QA en cada fase.
3. Compara diferentes modelos de SDLC y discute las ventajas y desventajas de cada uno.

### Tipos de Pruebas
1. Realiza una investigación sobre cada tipo de prueba y proporciona ejemplos de cada una.
2. Crea un cuadro comparativo que resuma las características principales de cada tipo de prueba.
3. Discute la importancia de las pruebas de regresión y cómo se implementan en un ciclo de desarrollo ágil.

### Ejercicios Teóricos Adicionales
1. Investiga y explica la importancia de las auditorías de calidad en el proceso de QA.
2. Describe el proceso de revisión de requisitos y su importancia en QA.
3. Define y explica el término "Mejora Continua" en el contexto de QA.
4. Investiga sobre los diferentes estándares de calidad (ISO, IEEE) y su aplicación en QA.
5. Explica la relación entre QA y la satisfacción del cliente.

## Comparación
Compara tus respuestas con el archivo `solucion_que_es_QA.md` para verificar tu comprensión.
```

### 01_Introduccion_QA/ejercicios/solucion_que_es_QA.md

```markdown
# Solución al Ejercicio: ¿Qué es QA?

## Diferencias entre QA y QC
QA (Aseguramiento de la Calidad) se centra en prevenir defectos en el proceso de desarrollo, mientras que QC (Control de Calidad) se enfoca en identificar y corregir defectos en el producto final.

### QA (Aseguramiento de la Calidad)
- **Enfoque:** Preventivo
- **Objetivo:** Mejorar los procesos de desarrollo y producción para evitar defectos.
- **Actividades:** Revisión de requisitos, auditorías de calidad, capacitación.

### QC (Control de Calidad)
- **Enfoque:** Reactivo
- **Objetivo:** Identificar y corregir defectos en los productos finales.
- **Actividades:** Pruebas de software, inspección, revisiones.

## Fases del SDLC y Rol de QA
### Planificación
- **Objetivo:** Definir los objetivos y el alcance del proyecto.
- **Actividades de QA:** Asegurar que los objetivos sean claros y alcanzables, y que los requisitos de calidad se integren desde el inicio.

### Análisis de Requisitos
- **Objetivo:** Recopilar y analizar los requisitos del sistema.
- **Actividades de QA:** Verificar que los requisitos sean completos, claros y verificables, y que contemplen criterios de calidad.

### Diseño
- **Objetivo:** Crear la arquitectura y el diseño del sistema.
- **Actividades de QA:** Revisar y validar los diseños para asegurar que cumplen con los requisitos y estándares de calidad.

### Desarrollo
- **Objetivo:** Codificación y construcción del sistema.
- **Actividades de QA:** Asegurar la adherencia a los estándares de codificación y realizar revisiones de código.

### Pruebas
- **Objetivo:** Verificación y validación del sistema.
- **Actividades de QA:** Planificar, diseñar, ejecutar y reportar las pruebas para asegurar que el sistema cumple con los requisitos y expectativas.

### Implementación
- **Objetivo:** Despliegue del sistema en el entorno de producción.
- **Actividades de QA:** Validar el despliegue y realizar pruebas post-implementación para asegurar una transición suave.

### Mantenimiento
- **Objetivo:** Realización de cambios y mejoras en el sistema.
- **Actividades de QA:** Asegurar que los cambios no introduzcan nuevos defectos y que el sistema continúe cumpliendo con los estándares de calidad.

## Comparación de Modelos de SDLC
### Modelo en Cascada
- **Ventajas:** Proceso estructurado, fácil de entender y gestionar.
- **Desventajas:** Poco flexible, difícil de volver a fases anteriores.

### Modelo en V
- **Ventajas:** Incluye actividades de prueba en paralelo, asegura una mayor calidad.
- **Desventajas:** Similar al modelo en cascada en términos de rigidez.

### Modelo Iterativo
- **Ventajas:** Permite mejoras continuas, adaptación a cambios.
- **Desventajas:** Requiere más gestión y puede ser más costoso.

### Modelo Ágil
- **Ventajas:** Alta flexibilidad, entrega continua de valor, colaboración constante.
- **Desventajas:** Requiere alta disciplina y colaboración del equipo, puede ser difícil de escalar.

## Tipos de Pruebas
### Pruebas Unitarias
- **Definición:** Verifican el funcionamiento de unidades individuales de código (métodos, funciones, clases).
- **Ejemplo:** Probar una función matemática para verificar que devuelve el resultado esperado.

### Pruebas de Integración
- **Definición:** Verifican la interacción entre diferentes unidades de código.
- **Ejemplo:** Probar la interacción entre un módulo de base de datos y una interfaz de usuario.

### Pruebas de Sistema
- **Definición:** Verifican el sistema completo para asegurar que cumple con los requisitos.
- **Ejemplo:** Probar todo el sistema de gestión de inventarios para asegurarse de que todas las funcionalidades trabajen como se espera.

### Pruebas de Aceptación
- **Definición:** Verifican que el sistema cumple con los criterios de aceptación y está listo para su despliegue.
- **Ejemplo:** Realizar pruebas de aceptación del usuario (UAT) para validar que el sistema cumple con los requisitos del cliente.

### Pruebas Funcionales
- **Definición:** Verifican que el sistema cumple con los requisitos funcionales especificados.
- **Ejemplo:** Probar una funcionalidad de login para verificar que los usuarios puedan iniciar sesión correctamente.

### Pruebas No Funcionales
- **Definición:** Verifican aspectos como rendimiento, seguridad y usabilidad del sistema.
- **Ejemplo:** Realizar pruebas de carga para asegurarse de que el sistema pueda manejar un alto volumen de usuarios simultáneos.

### Pruebas de Regresión
- **Definición:** Verifican que los cambios recientes no hayan introducido nuevos defectos en el sistema.
- **Importancia:** Aseguran que el sistema sigue funcionando correctamente después de realizar cambios o adiciones.

## Comparación de Tipos de Pruebas
| Tipo de Prueba       | Definición                                                                 | Ejemplo                                                        |
|----------------------|---------------------------------------------------------------------------|----------------------------------------------------------------|
| Pruebas Unitarias    | Verifican unidades individuales de código                                  | Probar una función matemática                                  |
| Pruebas de Integración| Verifican la interacción entre diferentes unidades de código              | Probar la interacción entre un módulo de base de datos y una interfaz de usuario |
| Pruebas de Sistema   | Verifican el sistema completo                                              | Probar todo el sistema de gestión de inventarios               |
| Pruebas de Aceptación| Verifican que el sistema cumple con los criterios de aceptación            | Pruebas de aceptación del usuario (UAT)                        |
| Pruebas Funcionales  | Verifican que el sistema cumple con los requisitos funcionales especificados| Probar una funcionalidad de login                              |
| Pruebas No Funcionales| Verifican aspectos como rendimiento, seguridad y usabilidad                | Pruebas de carga                                               |
| Pruebas de Regresión | Verifican que los cambios recientes no hayan introducido nuevos defectos   | Reejecutar pruebas anteriores después de cambios               |

## Implementación de Pruebas de Regresión en un Ciclo Ágil
En un ciclo de desarrollo ágil, las pruebas de regresión se implementan de la siguiente manera:
1. **Automatización de Pruebas:** Automatizar las pruebas para asegurar que se ejecuten rápidamente y con frecuencia.
2. **Integración Continua:** Integrar las pruebas de regresión en el proceso de integración continua para detectar defectos lo antes posible.
3. **Revisión y Actualización de Pruebas:** Revisar y actualizar las pruebas de regresión regularmente para asegurarse de que cubran todas las áreas críticas del sistema.

## Importancia de las Auditorías de Calidad
Las auditorías de calidad son importantes en QA porque:
- Aseguran que los procesos y procedimientos se adhieren a los estándares de calidad.
- Identifican áreas de mejora en el proceso de desarrollo.
- Proveen una evaluación independiente y objetiva de los procesos de calidad.

## Revisión de Requisitos
La revisión de requisitos es crucial en QA para:
- Asegurar que los requisitos sean claros, completos y verificables.
- Identificar posibles problemas o ambigüedades en los requisitos temprano en el proceso.
- Facilitar una mejor planificación y ejecución de las pruebas.

## Mejora Continua
La Mejora Continua en QA implica:
- Evaluar constantemente los procesos y procedimientos para identificar oportunidades de mejora

.
- Implementar cambios basados en feedback y resultados de auditorías.
- Fomentar una cultura de calidad y excelencia en toda la organización.

## Estándares de Calidad (ISO, IEEE)
- **ISO (Organización Internacional de Normalización):** Provee estándares globales que aseguran la calidad, seguridad y eficiencia de productos y servicios.
- **IEEE (Instituto de Ingenieros Eléctricos y Electrónicos):** Provee estándares específicos para la industria del software, incluyendo procesos de calidad y gestión de proyectos.

## Relación entre QA y Satisfacción del Cliente
QA está directamente relacionado con la satisfacción del cliente porque:
- Asegura que el producto final cumpla con las expectativas y requisitos del cliente.
- Reduce la probabilidad de defectos y fallas en el producto.
- Mejora la confianza del cliente en la organización y sus productos.