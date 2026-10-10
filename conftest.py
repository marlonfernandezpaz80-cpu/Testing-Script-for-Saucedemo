import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.menu_page import MenuPage
@pytest.fixture(scope="session", autouse=True)
def terminal():
    print("\nHa comenzado el Proceso de Testing de Saucedemo")
    yield
    print("Ha finalizado el Proceso de Testing de Saucedemo")

@pytest.fixture(scope="function")
def logged_page(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    inventory_page.is_loaded()
    yield inventory_page

@pytest.fixture(scope="function")
def problem_logged_page(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("problem_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    inventory_page.is_loaded()
    yield inventory_page

@pytest.fixture(scope="function")
def visual_user_logged_page(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("visual_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    inventory_page.is_loaded()
    yield inventory_page

@pytest.fixture(scope="function")
def full_cart_page(page: Page):
    products = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Test.allTheThings() T-Shirt (Red)"]
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    inventory_page.is_loaded()
    inventory_page.add_to_cart(products[0])
    inventory_page.add_to_cart(products[1])
    inventory_page.add_to_cart(products[2])
    inventory_page.open_cart()
    cart_page = CartPage(page)
    cart_page.is_loaded()
    yield cart_page


@pytest.fixture(scope="function")
def outchecked_page(page: Page, full_cart_page):
    full_cart_page.checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.step_one_is_loaded()
    checkout_page.fill_user_form("Marlon", "Fernandez", "12345")
    checkout_page.click_continue()
    checkout_page.step_two_is_loaded()
    checkout_page.click_finish()
    checkout_page.step_three_is_loaded()
    yield checkout_page

@pytest.fixture(scope="function")
def login_page(page: Page):
    login = LoginPage(page)
    login.open()
    yield login

@pytest.fixture(scope="function")
def logged_menu(page: Page, logged_page):
    menu_page = MenuPage(page)
    menu_page.open_menu()
    menu_page.is_loaded()
    yield menu_page


    