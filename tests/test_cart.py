import pytest
from playwright.sync_api import Page, expect
from pages.inventory_item_page import InventoryItemPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_get_out(page: Page, logged_page):
    logged_page.open_cart()
    cart_page = CartPage(page)
    cart_page.is_loaded()
    cart_page.get_out()
    inventory_page = InventoryPage(page)
    inventory_page.is_loaded()

@pytest.mark.smoke
def test_remove_product(page: Page, logged_page):
    product = "Sauce Labs Backpack"
    logged_page.add_to_cart(product)
    logged_page.open_cart()
    cart_page = CartPage(page)
    cart_page.is_loaded()
    cart_page.remove_from_cart(product)

