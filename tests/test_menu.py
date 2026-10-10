from playwright.sync_api import Page, expect
from pages.menu_page import MenuPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import pytest

@pytest.mark.regression
def test_close_menu(logged_menu):
    logged_menu.close_menu()
    logged_menu.is_not_loaded()

@pytest.mark.regression
def test_all_items_button_out_of_inventory(page: Page, logged_page):
    logged_page.open_cart()
    cart_page = CartPage(page)
    cart_page.is_loaded()
    menu_page = MenuPage(page)
    menu_page.open_menu()
    menu_page.click_all_items()
    menu_page.is_not_loaded()
    inventory_page = InventoryPage(page)
    inventory_page.is_loaded()

@pytest.mark.regression
def test_all_items_button_in_inventory(page: Page, logged_menu):
    logged_menu.click_all_items()
    logged_menu.is_loaded()
    logged_menu.close_menu()
    logged_menu.is_not_loaded()
    inventory_page = InventoryPage(page)
    inventory_page.is_loaded()

@pytest.mark.smoke
def test_logout(page: Page, logged_menu):
    logged_menu.click_logout()
    login_page = LoginPage(page)
    login_page.is_loaded()

@pytest.mark.regression
def test_about(page: Page, logged_menu):
    logged_menu.click_about()
    expect(page).to_have_url("https://saucelabs.com/")

@pytest.mark.regression
def test_reset_app_state(page: Page, full_cart_page):
    full_cart_page.get_out()
    inventory_page = InventoryPage(page)
    inventory_page.shopping_cart_badge_is_visible()
    menu_page = MenuPage(page)
    menu_page.open_menu()
    menu_page.is_loaded()
    menu_page.click_reset_app_state()
    menu_page.close_menu()
    inventory_page = InventoryPage(page)
    inventory_page.shopping_cart_badge_is_not_visible()
    full_cart_page.open()
    full_cart_page.products_are_not_visible()