### 04_Page Object Model (POM)

## Objetivos

- Entender qué es el Page Object Model (POM) y por qué es útil en la automatización de pruebas.
- Aprender a implementar el patrón POM en proyectos de Selenium.
- Ver ejemplos prácticos de cómo organizar y estructurar código utilizando POM.
- Conocer las mejores prácticas para trabajar con POM.

## Contenido

### ¿Qué es el Page Object Model (POM)?

El Page Object Model (POM) es un patrón de diseño que se utiliza en la automatización de pruebas para crear una abstracción de las páginas de la aplicación web que se está probando. Cada página de la aplicación se representa como una clase en el código, y los elementos de la página se representan como variables de la clase. Las interacciones con los elementos de la página se implementan como métodos de la clase.

### Beneficios del Page Object Model

- **Mantenibilidad**: Separar la lógica de la interfaz de usuario de la lógica de prueba facilita la actualización de las pruebas cuando cambia la interfaz de usuario.
- **Reusabilidad**: Los métodos de la página pueden ser reutilizados en diferentes scripts de prueba.
- **Claridad**: Mejora la legibilidad y organización del código de prueba.

### Implementación del Page Object Model

#### Estructura del Proyecto

Una estructura de proyecto típica utilizando POM podría verse así:

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

### Ejemplo Práctico de Page Object Model

#### Archivo `base_page.py`

Este archivo contiene la clase base que proporciona métodos comunes a todas las páginas.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_for_page_load()

    def wait_for_page_load(self, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

    def find_element(self, by, value, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))
            return element
        except Exception as e:
            logging.error(f"Error finding element by {by} with value {value}: {e}")
            self.capture_screenshot(f"error_{by}_{value}")
            return None

    def click_element(self, by, value, timeout=20):
        element = self.find_element(by, value, timeout)
        if element:
            element.click()

    def enter_text(self, by, value, text, timeout=20):
        element = self.find_element(by, value, timeout)
        if element:
            element.clear()
            element.send_keys(text)

    def capture_screenshot(self, name="screenshot"):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{name}_{timestamp}.png"
        screenshot_path = os.path.join("screenshots", screenshot_name)
        self.driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot saved to {screenshot_path}")
```

#### Archivo `home_page.py`

Este archivo contiene la clase que representa la página de inicio.

```python
from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils.locator import HomePageLocators

class HomePage(BasePage):
    URL = "https://www.example.com"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.URL)

    def click_customer_login(self):
        self.click_element(*HomePageLocators.CUSTOMER_LOGIN_BUTTON)
        return LoginPage(self.driver)

    def click_manager_login(self):
        self.click_element(*HomePageLocators.MANAGER_LOGIN_BUTTON)
```

#### Archivo `login_page.py`

Este archivo contiene la clase que representa la página de inicio de sesión.

```python
from pages.base_page import BasePage
from pages.main_page import MainPage
from utils.locator import LoginPageLocators

class LoginPage(BasePage):
    def login_user(self, username):
        self.enter_text(*LoginPageLocators.USERNAME_INPUT, username)
        self.click_element(*LoginPageLocators.LOGIN_BUTTON)
        return MainPage(self.driver)
```

#### Archivo `main_page.py`

Este archivo contiene la clase que representa la página principal.

```python
from pages.base_page import BasePage
from utils.locator import MainPageLocators
from selenium.webdriver.support.ui import Select

class MainPage(BasePage):
    def get_user_name(self):
        return self.find_element(*MainPageLocators.USER_NAME).text

    def select_account(self, account_number):
        select = Select(self.find_element(*MainPageLocators.ACCOUNT_SELECT))
        select.select_by_visible_text(account_number)

    def get_balance(self):
        return self.find_element(*MainPageLocators.BALANCE).text

    def click_logout(self):
        self.click_element(*MainPageLocators.LOGOUT_BUTTON)
```

#### Archivo `locator.py`

Este archivo contiene los localizadores para los elementos de la página.

```python
from selenium.webdriver.common.by import By

class HomePageLocators:
    CUSTOMER_LOGIN_BUTTON = (By.CSS_SELECTOR, '.btn.btn-customer')
    MANAGER_LOGIN_BUTTON = (By.CSS_SELECTOR, '.btn.btn-manager')

class LoginPageLocators:
    USERNAME_INPUT = (By.NAME, 'username')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.btn.btn-default')

class MainPageLocators:
    USER_NAME = (By.CSS_SELECTOR, '.user-name')
    ACCOUNT_SELECT = (By.ID, 'accountSelect')
    BALANCE = (By.CSS_SELECTOR, '.balance')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '.btn.logout')
```

#### Archivo `test_account_main_page.py`

Este archivo contiene las pruebas que utilizan las clases de página.

```python
import pytest
from pages.home_page import HomePage
from pages.main_page import MainPage

@pytest.mark.usefixtures("setup")
class TestAccountMainPage:
    def test_login(self, setup):
        home_page = HomePage(setup)
        login_page = home_page.click_customer_login()
        main_page = login_page.login_user("Harry Potter")
        assert main_page.get_user_name() == "Harry Potter"

    def test_select_account(self, setup):
        main_page = MainPage(setup)
        main_page.select_account("1001")
        assert main_page.get_balance() == "5000"
```

### Mejores Prácticas para Trabajar con POM

1. **Mantén tus clases de página simples**:
   - Cada clase debe representar una sola página de la aplicación.
   - Los métodos de la clase deben realizar acciones específicas en esa página.

2. **Utiliza localizadores claros y únicos**:
   - Asegúrate de que cada localizador sea único y fácil de identificar.
   - Almacena los localizadores en un archivo separado para mantener la clase de página limpia.

3. **Reutiliza métodos comunes**:
   - Si hay acciones comunes que se realizan en varias páginas, colócalas en la clase `BasePage` para reutilizarlas.

4. **Maneja las excepciones adecuadamente**:
   - Usa try-except para capturar errores y manejar excepciones.
   - Agrega logs y capturas de pantalla en caso de errores para facilitar la depuración.

### Manejo de Errores y Depuración

1. **Uso de Logs Detallados**:
   - Configura el logging para capturar información detallada sobre la ejecución del script.
   - Utiliza diferentes niveles de logging (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`) para categorizar los mensajes.

2. **Capturas de Pantalla para Errores**:
   - Captura capturas de pantalla cuando se produce un error para ayudar en la depuración.
   - Almacena las capturas de pantalla en una carpeta dedicada con nombres basados en la marca de tiempo.

3. **Análisis de Errores Comunes**:
   - **Elemento No Encontrado**: Verificar el selector, la visibilidad del elemento y la estructura del DOM.
   - **Errores de Tiempo de Espera**: Ajustar los tiempos de espera y usar condiciones de espera más específicas.
   - **Errores de Compatibilidad de Versión**: Asegurarse de que las versiones de Selenium, el controlador del navegador y el navegador sean compatibles entre sí.

### Ejemplo Completo de Page Object Model

A continuación se muestra un ejemplo completo que abarca varias páginas e interacciones, mostrando cómo se integran todos los componentes del POM.

#### home_page.py

```python
from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils.locator import HomePageLocators

class HomePage(BasePage):
    URL = "https://www.example.com

"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.URL)

    def click_customer_login(self):
        self.click_element(*HomePageLocators.CUSTOMER_LOGIN_BUTTON)
        return LoginPage(self.driver)

    def click_manager_login(self):
        self.click_element(*HomePageLocators.MANAGER_LOGIN_BUTTON)
```

#### login_page.py

```python
from pages.base_page import BasePage
from pages.main_page import MainPage
from utils.locator import LoginPageLocators

class LoginPage(BasePage):
    def login_user(self, username):
        self.enter_text(*LoginPageLocators.USERNAME_INPUT, username)
        self.click_element(*LoginPageLocators.LOGIN_BUTTON)
        return MainPage(self.driver)
```

#### main_page.py

```python
from pages.base_page import BasePage
from utils.locator import MainPageLocators
from selenium.webdriver.support.ui import Select

class MainPage(BasePage):
    def get_user_name(self):
        return self.find_element(*MainPageLocators.USER_NAME).text

    def select_account(self, account_number):
        select = Select(self.find_element(*MainPageLocators.ACCOUNT_SELECT))
        select.select_by_visible_text(account_number)

    def get_balance(self):
        return self.find_element(*MainPageLocators.BALANCE).text

    def click_logout(self):
        self.click_element(*MainPageLocators.LOGOUT_BUTTON)
```

#### test_account_main_page.py

```python
import pytest
from pages.home_page import HomePage
from pages.main_page import MainPage

@pytest.mark.usefixtures("setup")
class TestAccountMainPage:
    def test_login(self, setup):
        home_page = HomePage(setup)
        login_page = home_page.click_customer_login()
        main_page = login_page.login_user("Harry Potter")
        assert main_page.get_user_name() == "Harry Potter"

    def test_select_account(self, setup):
        main_page = MainPage(setup)
        main_page.select_account("1001")
        assert main_page.get_balance() == "5000"
```
