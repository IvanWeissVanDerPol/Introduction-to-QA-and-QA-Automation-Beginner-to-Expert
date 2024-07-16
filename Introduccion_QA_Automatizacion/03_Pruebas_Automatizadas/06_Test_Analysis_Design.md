# Análisis y Diseño de Pruebas

## Objetivos
- Entender el proceso de análisis y diseño de pruebas.
- Aprender a identificar condiciones y casos de prueba.
- Conocer diferentes técnicas de diseño de pruebas.

## Contenido

### ¿Qué es el Análisis de Pruebas?
El análisis de pruebas es el proceso de identificar qué debe probarse en el sistema. Implica la revisión de la documentación de requisitos y diseño para identificar las condiciones de prueba, que son aspectos del sistema que necesitan ser verificados.

#### Pasos del Análisis de Pruebas
1. **Revisión de Requisitos:** Evaluar los documentos de requisitos para identificar las funcionalidades y características que deben ser probadas.
2. **Identificación de Condiciones de Prueba:** Determinar las condiciones de prueba basadas en los requisitos. Cada condición representa un aspecto del sistema que debe ser verificado.
3. **Definición de Criterios de Aceptación:** Especificar los criterios que determinan si una condición de prueba pasa o falla.

### ¿Qué es el Diseño de Pruebas?
El diseño de pruebas es el proceso de crear casos de prueba y datos de prueba basados en las condiciones de prueba identificadas durante el análisis. Los casos de prueba son conjuntos específicos de entradas, acciones y resultados esperados que verifican una condición de prueba particular.

#### Pasos del Diseño de Pruebas
1. **Definición de Casos de Prueba:** Crear casos de prueba detallados que incluyan las entradas, las acciones a realizar y los resultados esperados.
2. **Preparación de Datos de Prueba:** Crear los datos necesarios para ejecutar los casos de prueba.
3. **Revisión de Casos de Prueba:** Evaluar los casos de prueba para asegurarse de que sean completos y efectivos.

### Técnicas de Diseño de Pruebas

#### Partición de Equivalencia
- **Descripción:** Dividir las entradas del sistema en particiones de equivalencia, donde todas las entradas en una partición deben ser tratadas de manera similar por el sistema.
- **Ejemplo:**
  - Para un campo de entrada que acepta números de 1 a 100, las particiones de equivalencia pueden ser: valores válidos (1-100), valores inválidos (<1 y >100).

#### Análisis de Valores Límite
- **Descripción:** Probar los límites de las particiones de equivalencia. Los defectos suelen ocurrir en los límites más que en el centro de las particiones.
- **Ejemplo:**
  - Para un campo de entrada que acepta números de 1 a 100, los valores límite serían: 0, 1, 100, 101.

#### Pruebas de Transición de Estados
- **Descripción:** Probar las transiciones entre diferentes estados del sistema.
- **Ejemplo:**
  - En una máquina expendedora, verificar las transiciones entre los estados de "espera", "selección de producto", "procesando pago", y "dispensando producto".

#### Pruebas Basadas en Casos de Uso
- **Descripción:** Crear casos de prueba basados en los casos de uso que describen las interacciones entre los usuarios y el sistema.
- **Ejemplo:**
  - Para un sistema de reservas, un caso de uso podría ser "reservar un vuelo", y los casos de prueba incluirían los diferentes escenarios de reserva.

#### Pruebas Exploratorias
- **Descripción:** Las pruebas exploratorias son menos estructuradas y se basan en la experiencia y el juicio del probador para identificar defectos.
- **Ejemplo:**
  - Navegar por una nueva aplicación sin casos de prueba predefinidos para encontrar problemas inesperados.

### Ejemplo de Diseño de Pruebas

#### Caso de Prueba: Validación de Campo de Edad
```markdown
## Caso de Prueba: Validación de Campo de Edad

### Condición de Prueba
El campo de edad debe aceptar solo valores entre 18 y 99.

### Casos de Prueba
1. **Caso de Prueba 1: Valor dentro del rango**
   - **Entrada:** 25
   - **Acción:** Ingresar 25 en el campo de edad y enviar el formulario.
   - **Resultado Esperado:** El formulario se envía exitosamente.

2. **Caso de Prueba 2: Valor por debajo del rango**
   - **Entrada:** 17
   - **Acción:** Ingresar 17 en el campo de edad y enviar el formulario.
   - **Resultado Esperado:** El sistema muestra un mensaje de error indicando que la edad debe estar entre 18 y 99.

3. **Caso de Prueba 3: Valor por encima del rango**
   - **Entrada:** 100
   - **Acción:** Ingresar 100 en el campo de edad y enviar el formulario.
   - **Resultado Esperado:** El sistema muestra un mensaje de error indicando que la edad debe estar entre 18 y 99.

4. **Caso de Prueba 4: Valor límite inferior**
   - **Entrada:** 18
   - **Acción:** Ingresar 18 en el campo de edad y enviar el formulario.
   - **Resultado Esperado:** El formulario se envía exitosamente.

5. **Caso de Prueba 5: Valor límite superior**
   - **Entrada:** 99
   - **Acción:** Ingresar 99 en el campo de edad y enviar el formulario.
   - **Resultado Esperado:** El formulario se envía exitosamente.
Conclusión
El análisis y diseño de pruebas son componentes críticos del proceso de testing. Utilizando técnicas de diseño de pruebas como partición de equivalencia, análisis de valores límite y pruebas basadas en casos de uso, se pueden crear casos de prueba efectivos que aseguren una cobertura adecuada y la calidad del sistema. La correcta identificación y documentación de condiciones de prueba y casos de prueba mejoran significativamente la capacidad de detectar y corregir defectos.

Tareas
Realiza un análisis de pruebas para un módulo de tu aplicación y documenta las condiciones de prueba.
Diseña al menos cinco casos de prueba para una funcionalidad específica de tu aplicación utilizando técnicas de diseño de pruebas.
Revisa los casos de prueba diseñados con un compañero y mejora los casos basados en la retroalimentación recibida.
