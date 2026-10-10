from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage
import pytest

@pytest.mark.smoke
@pytest.mark.parametrize("username", 
                         [("standard_user"),
                          ("performance_glitch_user"),
                          ("error_user")])
def test_login_successful(page: Page, username, login_page):
    login_page.login(username, "secret_sauce")
    inventory_login_page = InventoryPage(page)
    inventory_login_page.is_loaded()


@pytest.mark.regression
@pytest.mark.parametrize("username, password", [
    ("standard_user", "invalid_password"),
    ("invalid_user", "secret_sauce")])
def test_login_invalid_user_or_password(page: Page, username, password, login_page):
    login_page.login(username, password)
    expect(login_page.login_error_sign).to_be_visible()
    inventory_page = InventoryPage(page)
    expect(inventory_page.title).not_to_be_visible()

@pytest.mark.regression
@pytest.mark.parametrize("username, password", [
    ("standard_user", ""),
    ("", "secret_sauce")])
def test_login_empty_user_or_password(page: Page, username, password, login_page):
    login_page.login(username, password)
    expect(login_page.login_empty_box_sign).to_be_visible()
    inventory_page = InventoryPage(page)
    expect(inventory_page.title).not_to_be_visible()

@pytest.mark.regression
def test_login_locked_user(page: Page, login_page):
    login_page.login("locked_out_user", "secret_sauce")
    expect(login_page.login_locked_out_sign).to_be_visible()
    inventory_page = InventoryPage(page)
    expect(inventory_page.title).not_to_be_visible()



