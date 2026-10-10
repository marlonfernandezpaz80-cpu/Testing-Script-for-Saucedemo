# Testing Script for Saucedemo

Suite de pruebas automatizadas end-to-end para [Saucedemo](https://www.saucedemo.com), construida con **Python**, **Pytest** y **Playwright**, siguiendo el patrón de diseño **Page Object Model (POM)**.

---

## Tabla de contenidos

- [Descripción](#descripción)
- [Tecnologías](#tecnologías)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Cobertura de pruebas](#cobertura-de-pruebas)
- [Instalación](#instalación)
- [Ejecución de las pruebas](#ejecución-de-las-pruebas)
- [Decisiones de diseño](#decisiones-de-diseño)
- [Autor](#autor)

---

## Descripción

Este proyecto automatiza los flujos principales de la tienda demo Saucedemo: autenticación, catálogo de productos, carrito de compras, proceso de compra (checkout) y menú de navegación.

Además de los flujos exitosos, incluye pruebas para usuarios con comportamientos defectuosos conocidos de la aplicación (`problem_user`, `visual_user`, `locked_out_user`), con el objetivo de detectar y documentar sus fallos.

## Tecnologías

| Herramienta | Uso |
|---|---|
| Python 3 | Lenguaje principal |
| Pytest | Framework de pruebas, fixtures y marcadores |
| Playwright (sync API) | Automatización del navegador |
| pytest-playwright | Integración entre Pytest y Playwright |
| pypdf | Validación del contenido del PDF descargado |

## Estructura del proyecto

```
Testing-Script-for-Saucedemo/
├── pages/                      # Page Objects
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── inventory_item_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── menu_page.py
├── tests/                      # Casos de prueba
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_menu.py
├── conftest.py                 # Fixtures compartidas
├── pytest.ini                  # Configuración de Pytest
└── README.md
```

## Cobertura de pruebas

La suite cuenta con **33 pruebas**: 13 `smoke` y 20 `regression`.

| Módulo | Qué se valida |
|---|---|
| **Login** | Acceso exitoso (`standard_user`, `performance_glitch_user`, `error_user`), credenciales inválidas, campos vacíos y usuario bloqueado |
| **Inventario** | Añadir y quitar productos del carrito, detalle de producto, ordenamiento por nombre (A-Z / Z-A) y por precio (menor a mayor / mayor a menor) |
| **Usuarios con fallos** | Imágenes duplicadas y datos inconsistentes en `problem_user`; imágenes y precios incorrectos en `visual_user` |
| **Carrito** | Volver a la tienda y eliminar productos |
| **Checkout** | Flujo completo de compra, verificación de subtotal, impuestos y total, regreso al inicio y generación y validación de PDF del pedido |
| **Menú** | Abrir y cerrar menú, "All items", "About", "Reset App State" y "Logout" |

### Marcadores

Las pruebas están clasificadas con marcadores de Pytest:

- `smoke`: pruebas críticas, que validan los flujos esenciales.
- `regression`: pruebas no críticas, que amplían la cobertura.

## Instalación

**1. Clonar el repositorio**

```bash
git clone https://github.com/marlonfernandezpaz80-cpu/Testing-Script-for-Saucedemo.git
cd Testing-Script-for-Saucedemo
```

**2. Crear y activar un entorno virtual (recomendado)**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

**3. Instalar las dependencias**

```bash
pip install pytest pytest-playwright pypdf
```

**4. Instalar los navegadores de Playwright**

```bash
playwright install
```

## Ejecución de las pruebas

```bash
# Todas las pruebas
pytest

# Solo las pruebas críticas (smoke)
pytest -m smoke

# Solo las pruebas de regresión
pytest -m regression

# Un módulo específico
pytest tests/test_login.py

# Con el navegador visible
pytest --headed

# En otro navegador
pytest --browser firefox

# Salida detallada
pytest -v
```

> La URL base (`https://www.saucedemo.com`) está definida en `pytest.ini`, por lo que no es necesario configurarla manualmente.

## Decisiones de diseño

- **Page Object Model:** cada página tiene su propia clase con sus localizadores y acciones, lo que separa la lógica de interacción de las pruebas y facilita el mantenimiento.
- **Fixtures reutilizables:** `conftest.py` centraliza los flujos repetitivos (login, carrito lleno, compra finalizada, menú abierto), evitando duplicar código en los tests.
- **Localizadores semánticos:** se prioriza `get_by_role`, `get_by_placeholder` y `get_by_text`, más cercanos a lo que ve el usuario, antes que selectores CSS.
- **Esperas automáticas:** se usan aserciones `expect` de Playwright, que reintentan hasta cumplirse la condición, en lugar de pausas fijas.
- **Pruebas parametrizadas:** con `pytest.mark.parametrize` se cubren varios usuarios y productos sin repetir pruebas.

## Autor

**Marlon Fernandez Paz**
GitHub: [@marlonfernandezpaz80-cpu](https://github.com/marlonfernandezpaz80-cpu)
