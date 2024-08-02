### 03_Escribiendo Scripts con Selenium

## Objetivos

- Aprender a escribir scripts básicos con Selenium WebDriver.
- Comprender cómo localizar elementos web utilizando diferentes métodos.
- Realizar interacciones básicas con elementos web.
- Implementar estrategias de sincronización y esperas.
- Generar informes básicos con capturas de pantalla y logs.

## Contenido

### Primer Script con Selenium WebDriver

#### Estructura básica de un script Selenium

Un script básico de Selenium generalmente incluye los siguientes pasos:

1. Importar las bibliotecas necesarias.
2. Configurar el driver del navegador.
3. Navegar a la URL deseada.
4. Realizar interacciones con la página web.
5. Cerrar el navegador.

#### Abrir y cerrar el navegador

```python
from selenium import webdriver

# Configuración del driver para Chrome
driver = webdriver.Chrome()

# Abrir el navegador y navegar a una URL
driver.get('https://www.example.com')

# Cerrar el navegador
driver.quit()
```

### Localización de Elementos Web

### Ejemplo de HTML

A continuación se muestra un ejemplo de código HTML que contiene varios elementos de un formulario de búsqueda. Utilizaremos estos elementos para mostrar cómo localizarlos con diferentes métodos en Selenium.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Página de Ejemplo</title>
</head>
<body>
    <!-- Formulario de búsqueda -->
    <form id="search-form">
        <!-- Campo de entrada de texto para búsqueda -->
        <input type="text" name="q" id="search-input" class="search-box" placeholder="Buscar...">
        <!-- Botón de envío del formulario de búsqueda -->
        <button type="submit" class="search-button">Buscar</button>
    </form>
</body>
</html>
```

### Uso de Selectores CSS

Podemos usar selectores CSS para localizar el campo de búsqueda basado en su nombre (`name`), id (`id`), o clase (`class`).

```python
# Localizar por nombre
search_box = driver.find_element(By.CSS_SELECTOR, 'input[name="q"]')

# Localizar por id
search_box = driver.find_element(By.CSS_SELECTOR, '#search-input')

# Localizar por clase
search_box = driver.find_element(By.CSS_SELECTOR, '.search-box')
```

### Uso de XPath

XPath permite una localización más precisa basada en la estructura del documento HTML.

```python
# Localizar el campo de búsqueda por el atributo 'name'
search_box = driver.find_element(By.XPATH, '//input[@name="q"]')

# Localizar el campo de búsqueda por el atributo 'id'
search_box = driver.find_element(By.XPATH, '//input[@id="search-input"]')

# Localizar el botón de búsqueda por la clase
search_button = driver.find_element(By.XPATH, '//button[@class="search-button"]')
```

### Otros Métodos de Localización

#### Por Nombre (`By.NAME`)

```python
search_box = driver.find_element(By.NAME, 'q')
```

#### Por ID (`By.ID`)

```python
search_box = driver.find_element(By.ID, 'search-input')
```

#### Por Clase (`By.CLASS_NAME`)

```python
search_box = driver.find_element(By.CLASS_NAME, 'search-box')
```

#### Por Etiqueta (`By.TAG_NAME`)

```python
input_fields = driver.find_element(By.TAG_NAME, 'input')
```

### Resumen

Estos ejemplos muestran cómo localizar elementos en una página web utilizando diferentes estrategias con Selenium WebDriver. El código HTML de ejemplo proporciona una referencia clara para entender a qué elementos nos estamos refiriendo en los scripts de Selenium.

### Interacciones Básicas con Elementos Web

#### Hacer clic en elementos

```python
button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
button.click()
```

#### Introducir texto en campos de entrada

```python
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('laptop')
```

#### Enviar formularios

```python
search_box.send_keys(Keys.RETURN)
```

### Estrategias de Sincronización y Esperas

#### Esperas implícitas

Las esperas implícitas configuran Selenium para esperar un tiempo determinado antes de lanzar una excepción si no encuentra el elemento.

```python
driver.implicitly_wait(10)  # Esperar hasta 10 segundos
```

#### Esperas explícitas

Las esperas explícitas permiten esperar a que se cumpla una condición específica antes de continuar.

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'q'))
)
```

#### Esperas basadas en condiciones personalizadas

Puedes crear tus propias condiciones de espera personalizada utilizando funciones lambda.

```python
element = WebDriverWait(driver, 10).until(
    lambda d: d.find_element(By.NAME, 'q')
)
```

### Generación de Informes Básicos

#### Capturas de pantalla en caso de error

Puedes capturar capturas de pantalla cuando se produce un error o en cualquier momento de la ejecución del script.

```python
driver.save_screenshot('screenshot.png')
```

#### Logs básicos

Para mantener registros básicos de las acciones realizadas y los resultados.

```python
import logging

logging.basicConfig(filename='test.log', level=logging.INFO)
logging.info('Navegar a la página de ejemplo')
```

### Ejemplo Completo con Comentarios Explicativos

Este ejemplo completo incluye la configuración del driver, la navegación a una página de ejemplo, la búsqueda de un término, la verificación de los resultados, y la captura de una captura de pantalla en caso de error, junto con el uso de registros para monitorear la ejecución del script.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Configuración del logging
logging.basicConfig(filename='test.log', level=logging.INFO)

try:
    # Configuración del driver para Chrome
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Espera implícita

    logging.info('Navegar a la página de ejemplo')
    driver.get('https://www.example.com')

    # Encontrar el campo de búsqueda, introducir un término de búsqueda y enviar el formulario
    logging.info('Encontrar el campo de búsqueda')
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('Selenium')
    search_box.send_keys(Keys.RETURN)

    # Esperar a que los resultados de búsqueda aparezcan
    logging.info('Esperar a que los resultados de búsqueda aparezcan')
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'result'))
    )

    # Verificar que hay resultados de búsqueda
    assert 'resultados' in driver.page_source
    logging.info('Resultados de búsqueda encontrados')

    # Interactuar con una lista desplegable
    logging.info('Interactuar con una lista desplegable')
    select_element = Select(driver.find_element(By.ID, 'dropdown'))
    select_element.select_by_visible_text('Option 1')

    logging.info('Opción seleccionada en la lista desplegable')

except Exception as e:
    logging.error(f'Se produjo un error: {e}')
    driver.save_screenshot('error_screenshot.png')

finally:
    # Cerrar el navegador
    driver.quit()
```

### Mejores Prácticas al Escribir Scripts con Selenium

1. **Mantén tus scripts limpios y organizados**:
   - Divide tu código en funciones reutilizables.
   - Utiliza nombres descriptivos para tus variables y funciones.

2. **Usa el patrón Page Object Model (POM)**:
   - Organiza tu código creando clases para cada página de tu aplicación web.
   - Separa la lógica de la prueba de la lógica de la interfaz de usuario.

3. **Maneja excepciones de manera efectiva**:
   - Usa bloques try-except para capturar y manejar errores.
   - Agrega logs y capturas de pantalla en caso de errores para facilitar la depuración.

4. **Configura variables de entorno**:
   - Evita hardcoding de rutas y credenciales.
   - Usa variables de entorno para almacenar información sensible y rutas de drivers.

5. **Optimiza el uso de esperas**:
   - Prefiere las esperas explícitas sobre las implícitas para mayor control sobre las condiciones de espera.
   - Usa condiciones personalizadas cuando sea necesario.

### Ejemplos Adicionales

#### Interacción con Listas Desplegables

```python
from selenium.webdriver.support.ui import Select

# Seleccionar una opción por su texto visible
select = Select(driver.find_element(By.ID, 'dropdown'))
select.select_by_visible_text('Option 1')
```

#### Interacción con Casillas de Verificación

```python
# Seleccionar una casilla de verificación
checkbox = driver.find_element(By.ID, 'checkbox')
if not checkbox.is_selected():
    checkbox.click()
```

#### Interacción con Radio Buttons

```python
# Seleccionar un radio button
radio_button = driver.find_element(By.ID, 'radio')
radio_button.click()
```

#### Manejo de Ventanas Emergentes (Pop-ups)

```python
# Aceptar una alerta
alert = driver.switch_to.alert
alert.accept()

# Cancelar una alerta
alert.dismiss()
```

#### Manejo de iframes

```python
# Cambiar a un iframe usando su nombre o ID


driver.switch_to.frame('iframe_name_or_id')

# Volver al contenido principal
driver.switch_to.default_content()
```

### Manejo de Errores y Depuración

#### Uso de Logs Detallados

```python
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Este es un mensaje de depuración')
```

#### Capturas de Pantalla para Errores

```python
try:
    # Intentar encontrar un elemento
    element = driver.find_element(By.ID, 'non_existent_id')
except Exception as e:
    logging.error(f'Se produjo un error: {e}')
    driver.save_screenshot('error_screenshot.png')
```

#### Análisis de Errores Comunes

1. **Elemento No Encontrado**:
   - Verificar que el selector utilizado es correcto.
   - Asegurarse de que el elemento esté presente en el DOM antes de interactuar con él (usar esperas explícitas).

2. **Errores de Tiempo de Espera**:
   - Aumentar el tiempo de espera para elementos que tardan más en cargarse.
   - Utilizar condiciones de espera más específicas.

3. **Errores de Compatibilidad de Versión**:
   - Asegurarse de que las versiones de Selenium, el controlador del navegador y el navegador sean compatibles entre sí.
