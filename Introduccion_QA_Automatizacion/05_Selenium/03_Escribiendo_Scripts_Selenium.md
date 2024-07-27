### 05_Selenium_Basico/03_Escribiendo_Scripts_Selenium.md

# Escribiendo Scripts con Selenium

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
driver.get('https://nissei.com/py/')

# Cerrar el navegador
driver.quit()
```

#### Navegar a una URL

```python
driver.get('https://nissei.com/py/')
```
### 05_Selenium_Basico/03_Escribiendo_Scripts_Selenium.md

## Localización de Elementos Web

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
logging.info('Navegar a la página de Nissei')
```

### Ejemplo Completo

Este ejemplo completo incluye la configuración del driver, la navegación a la página de Nissei, la búsqueda de un término, la verificación de los resultados, y la captura de una captura de pantalla en caso de error, junto con el uso de registros para monitorear la ejecución del script.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import chromedriver_binary  # Adds chromedriver binary to path

# Configuración del logging
logging.basicConfig(filename='test.log', level=logging.INFO)

try:
    # Configuración del driver para Chrome
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Espera implícita

    logging.info('Navegar a la página de Nissei')
    driver.get('https://nissei.com/py/')

    # Encontrar el campo de búsqueda, introducir un término de búsqueda y enviar el formulario
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('laptop')
    search_box.send_keys(Keys.RETURN)

    # Esperar a que los resultados de búsqueda aparezcan
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'product-list'))
    )

    # Verificar que hay resultados de búsqueda
    assert 'resultados' in driver.page_source

    logging.info('Resultados de búsqueda encontrados')

except Exception as e:
    logging.error(f'Se produjo un error: {e}')
    driver.save_screenshot('error_screenshot.png')

finally:
    # Cerrar el navegador
    driver.quit()
```

### Ejercicio de Ejemplo

**Objetivo:** Navegar a la página de Nissei, buscar un producto, verificar que se muestran resultados y capturar una captura de pantalla.

1. **Navegar a la página de Nissei:**
   - Usar Selenium WebDriver para abrir Chrome y navegar a `https://nissei.com/py/`.

2. **Buscar un producto:**
   - Encontrar el campo de búsqueda utilizando `By.NAME`.
   - Introducir el término "laptop" en el campo de búsqueda.
   - Enviar el formulario de búsqueda.

3. **Verificar los resultados:**
   - Esperar a que los resultados de búsqueda aparezcan utilizando una espera explícita.
   - Verificar que la página contiene los resultados de búsqueda.

4. **Capturar una captura de pantalla:**
   - Capturar una captura de pantalla en caso de error y también después de verificar los resultados.

5. **Cerrar el navegador:**
   - Asegurarse de que el navegador se cierra al final del script.

**Código de ejemplo:**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import chromedriver_binary  # Adds chromedriver binary to path

# Configuración del logging
logging.basicConfig(filename='test.log', level=logging.INFO)

try:
    # Configuración del driver para Chrome
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Espera implícita

    logging.info('Navegar a la página de Nissei')
    driver.get('https://nissei.com/py/')

    # Encontrar el campo de búsqueda, introducir un término de búsqueda y enviar el formulario
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('laptop')
    search_box.send_keys(Keys.RETURN)

    # Esperar a que los resultados de búsqueda aparezcan
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'product-list'))
    )

    # Verificar que hay resultados de búsqueda
    assert 'resultados' in driver.page_source

    logging.info('Resultados de búsqueda encontrados')

    # Capturar una captura de pantalla de los resultados
    driver.save_screenshot('resultados_busqueda.png')

except Exception as e:
    logging.error(f'Se produjo un error: {e}')
    driver.save_screenshot('error_screenshot.png')

finally:
    # Cerrar el navegador
    driver.quit()
```

Este script completa los pasos necesarios para buscar un producto en la página de Nissei, verificar los resultados y manejar errores capturando capturas de pantalla y registros de logs.