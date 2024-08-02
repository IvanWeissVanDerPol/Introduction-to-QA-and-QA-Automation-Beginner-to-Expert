### Configuración de Selenium

## Objetivos

- Configurar el entorno de desarrollo en diferentes sistemas operativos para utilizar Selenium de manera eficiente.
- Configurar el PATH para los drivers del navegador.
- Entender la estructura y configuración del proyecto de pruebas.

## Contenido

### Configuración en Diferentes SO

#### Windows

1. **Instalar Python**:
   - Descarga el instalador de Python desde [python.org](https://www.python.org/downloads/windows/).
   - Durante la instalación, selecciona "Add Python to PATH".

2. **Instalar Selenium**:
   ```sh
   pip install selenium
   ```

3. **Descargar y Configurar ChromeDriver**:
   - Descarga ChromeDriver desde [aquí](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Extrae el ejecutable y colócalo en un directorio que esté en tu PATH del sistema.

### Configuración del Entorno de Desarrollo

### Estructura del Proyecto

Para mantener tu proyecto organizado y manejable, sigue una estructura de directorios como la siguiente:

```
project/
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── main_page.py
│   └── transaction_page.py
│
├── tests/
│   ├── base_test.py
│   ├── test_account_main_page.py
│   ├── test_customer_login_page.py
│   ├── test_deposit_page.py
│   ├── test_full_workflow.py
│   ├── test_home_page.py
│   └── test_withdraw_page.py
│
├── utils/
│   ├── locator.py
│   └── utils.py
│
├── conftest.py
└── requirements.txt
```

### Explicación de la Configuración del Proyecto

#### conftest.py

El archivo `conftest.py` es utilizado por `pytest` para configurar el entorno de pruebas. Aquí se configura el logging y se define una fixture que inicializa y cierra el WebDriver para las pruebas.

```python
import pytest
import logging

def pytest_configure(config):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
        logging.FileHandler("test_log.log"),
        logging.StreamHandler()
    ])

@pytest.fixture(scope='session')
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
```

- **Configuración de Logging**: Se configura el logging para capturar información de depuración y errores. Los logs se guardan en un archivo `test_log.log` y también se muestran en la consola.
- **Fixture `driver`**: Define el ciclo de vida del WebDriver, desde su inicialización hasta su cierre, utilizando `yield` para proporcionar el WebDriver a las pruebas.

#### utils/utils.py

Este archivo contiene funciones de utilidad para manejar esperas explícitas y otras tareas comunes.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

def wait_for_page_load(driver, timeout=20):
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script('return document.readyState') == 'complete'
    )

def wait_for_element(driver, by, value, timeout=20):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))

def login_user(driver, username):
    from pages.home_page import HomePage
    from pages.login_page import LoginPage

    logging.info(f"Logging in user: {username}")
    homepage = HomePage(driver)
    homepage.click_customer_login()
    logging.info("Navigated to Customer Login page")
    login_page = LoginPage(driver)
    login_page.login_user(username)
    logging.info(f"User {username} logged in successfully")
```

- **wait_for_page_load**: Espera hasta que la página esté completamente cargada.
- **wait_for_element**: Espera hasta que un elemento específico sea visible en la página.
- **login_user**: Realiza el proceso de inicio de sesión para un usuario específico.

#### pages/base_page.py

La clase `BasePage` proporciona métodos comunes para interactuar con elementos de la página.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from utils.utils import wait_for_page_load
import os
import time
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        wait_for_page_load(self.driver)
        logging.info("Page loaded successfully.")

    def find_element(self, locator, timeout=20) -> WebElement or None:
        try:
            logging.info(f"Trying to find element by {locator[0]} with value {locator[1]}")
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((locator[0], locator[1])))
            logging.info(f"Element found: {locator[0]} with value {locator[1]}")
            return element
        except Exception as e:
            logging.error(f"Error finding element by {locator[0]} with value {locator[1]}: {e}")
            self.capture_screenshot(f"error_{locator[0]}_{locator[1]}")
            return None
        
    def find_elements(self, locator, timeout=20) -> list[WebElement] or None:
        try:
            logging.info(f"Trying to find elements by {locator[0]} with value {locator[1]}")
            elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((locator[0], locator[1])))
            logging.info(f"Elements found: {locator[0]} with value {locator[1]}")
            return elements
        except Exception as e:
            logging.error(f"Error finding elements by {locator[0]} with value {locator[1]}: {e}")
            self.capture_screenshot(f"error_{locator[0]}_{locator[1]}")
            return []

    def click_element(self, locator, timeout=20):
        logging.info(f"Attempting to click element by {locator[0]} with value {locator[1]}")
        element = self.find_element(locator, timeout)
        if element:
            element.click()
            logging.info(f"Clicked element by {locator[0]} with value {locator[1]}")
        else:
            logging.error(f"Failed to click element by {locator[0]} with value {locator[1]}")

    def enter_text(self, locator, text, timeout=

20):
        logging.info(f"Attempting to enter text into element by {locator[0]} with value {locator[1]}")
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
            logging.info(f"Entered text '{text}' into element by {locator[0]} with value {locator[1]}")
        else:
            logging.error(f"Failed to enter text into element by {locator[0]} with value {locator[1]}")

    def capture_screenshot(self, name="screenshot"):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{name}_{timestamp}.png"
        screenshot_path = os.path.join("screenshots", screenshot_name)
        self.driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot saved to {screenshot_path}")
```

- **find_element**: Encuentra un único elemento en la página usando un localizador específico.
- **find_elements**: Encuentra múltiples elementos en la página.
- **click_element**: Hace clic en un elemento localizado.
- **enter_text**: Ingresa texto en un campo de entrada localizado.
- **capture_screenshot**: Captura una captura de pantalla y la guarda con un nombre basado en la marca de tiempo.

