
# Configuración de Selenium

## Objetivos

- Aprender a instalar Selenium y el driver necesario para Chrome.
- Configurar el entorno de desarrollo en Windows para utilizar Selenium de manera eficiente.
- Integrar Selenium con VSCode.
- Configurar el PATH para los drivers del navegador.

## Contenido

### Instalación de Selenium

#### Instalación de Selenium WebDriver con pip

Para instalar Selenium WebDriver en tu entorno de Python, puedes utilizar pip, el gestor de paquetes de Python. Ejecuta el siguiente comando en tu terminal:

```bash
pip install selenium
```

#### Descarga e Instalación de ChromeDriver

Para facilitar la instalación de ChromeDriver, utilizaremos el paquete `chromedriver-py`, que instala automáticamente la versión adecuada de ChromeDriver. Ejecuta el siguiente comando en tu terminal:

```bash
pip install chromedriver-py
```

Esto instalará ChromeDriver y lo hará disponible en tu entorno de Python.

### Configuración del Entorno de Desarrollo

#### Integración con VSCode

1. Abre VSCode y crea un nuevo proyecto o abre un proyecto existente.
2. Abre la terminal integrada (`Ctrl + '`).
3. Asegúrate de que el entorno virtual (si lo tienes) esté activado y que Selenium y ChromeDriver estén instalados. Si no, instálalos usando:

   ```bash
   pip install selenium chromedriver-py
   ```

### Ejemplo de Configuración en un Script Python

Una vez que tengas Selenium y ChromeDriver configurados, puedes probar tu instalación con un script Python simple. Asegúrate de que `chromedriver.exe` esté en el directorio de tu proyecto.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_binary  # Adds chromedriver binary to path

# Configuración del driver para Chrome
driver = webdriver.Chrome()

# Navegar a la página de Nissei
driver.get('https://nissei.com/py/')

# Encontrar el campo de búsqueda, introducir un término de búsqueda y enviar el formulario
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('laptop')
search_box.send_keys(Keys.RETURN)

# Verificar que hay resultados de búsqueda
assert 'resultados' in driver.page_source

# Cerrar el navegador
driver.quit()
```

Este script debería abrir una instancia de Chrome, navegar a "https://nissei.com/py/", buscar el término "laptop", verificar que hay resultados de búsqueda y luego cerrar el navegador.
