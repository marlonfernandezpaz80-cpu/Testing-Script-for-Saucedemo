from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import Page, expect
from pypdf import PdfReader
import pytest

def calculate_subtotal_price(prices_list):
    subtotal_price = 0
    for price in prices_list:
        subtotal_price += price
    subtotal_price = round(subtotal_price, 2)
    return subtotal_price


@pytest.mark.smoke
def test_checkout_flux(page: Page, full_cart_page):
    prices_list = full_cart_page.get_prices_list()
    expected_subtotal = calculate_subtotal_price(prices_list)
    full_cart_page.checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.step_one_is_loaded()
    checkout_page.fill_user_form("Marlon", "Fernandez", "12345")
    checkout_page.click_continue()
    checkout_page.step_two_is_loaded()
    subtotal_price = checkout_page.get_subtotal_price()
    assert expected_subtotal == subtotal_price
    tax = checkout_page.get_tax()
    expected_total = round((subtotal_price + tax), 2)
    total = checkout_page.get_total_price()
    assert expected_total == total
    checkout_page.click_finish()
    checkout_page.step_three_is_loaded()

@pytest.mark.smoke
def test_back_home(page: Page, outchecked_page):
    outchecked_page.back_home()
    inventory_page = InventoryPage(page)
    inventory_page.is_loaded()

@pytest.mark.smoke
def test_generate_pdf(outchecked_page, page: Page, tmp_path):
    with page.expect_download() as download_info:
        outchecked_page.generate_pdf()
    download = download_info.value
    ruta = tmp_path / download.suggested_filename
    download.save_as(ruta)
    assert ruta.exists()
    reader = PdfReader(ruta)
    document_page = reader.pages[0]
    page_text = document_page.extract_text()
    assert "Order Receipt" in page_text