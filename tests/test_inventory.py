import pytest
from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage
from pages.inventory_item_page import InventoryItemPage
from pages.cart_page import CartPage

@pytest.mark.smoke
@pytest.mark.parametrize("product", [("Sauce Labs Backpack"), ("Test.allTheThings() T-Shirt (Red)")])
def test_add_to_cart_and_remove_from_cart(logged_page, page: Page, product):
    logged_page.add_to_cart(product)
    cart = CartPage(page)
    cart.open()
    cart.product_exists(product)
    logged_page.open()
    logged_page.remove_from_cart(product)
    cart.open()
    cart.product_do_not_exists(product)

@pytest.mark.smoke
@pytest.mark.parametrize("product", [("Sauce Labs Backpack"), ("Test.allTheThings() T-Shirt (Red)")])
def test_get_product_description(logged_page, page: Page, product):
    logged_page.get_product_description(product)
    item_page = InventoryItemPage(page)
    item_page.is_loaded()
    item_page.product_exists(product)

@pytest.mark.regression
def test_order_inventory_name_az(logged_page):
    logged_page.order_inventory_name_az()
    titles_list = logged_page.get_list_of_titles()
    sorted_list = sorted(titles_list, reverse=False)
    assert titles_list == sorted_list

@pytest.mark.regression
def test_order_inventory_name_za(logged_page):
    logged_page.order_inventory_name_za()
    titles_list = logged_page.get_list_of_titles()
    sorted_list = sorted(titles_list, reverse=True)
    assert titles_list == sorted_list

@pytest.mark.regression
def test_order_inventory_price_lohi(logged_page):
    logged_page.order_inventory_price_lohi()
    prices_list = logged_page.get_list_of_prices()
    new_prices_list = []
    for price in prices_list:
        price = float(price[1:])
        new_prices_list.append(price)
    sorted_list = sorted(new_prices_list, reverse=False)
    assert new_prices_list == sorted_list

@pytest.mark.regression
def test_order_inventory_price_hilo(logged_page):
    logged_page.order_inventory_price_hilo()
    prices_list = logged_page.get_list_of_prices()
    new_prices_list = []
    for price in prices_list:
        price = float(price[1:])
        new_prices_list.append(price)
    sorted_list = sorted(new_prices_list, reverse=True)
    assert new_prices_list == sorted_list

@pytest.mark.regression
def test_problem_user_inventory_images(problem_logged_page):
    src_list = problem_logged_page.get_src_list()
    src_set = set(src_list)
    assert len(src_list) != len(src_set)

@pytest.mark.regression
@pytest.mark.parametrize("product", [("Sauce Labs Backpack"), ("Test.allTheThings() T-Shirt (Red)")])
def test_problem_user_get_description(problem_logged_page, page: Page, product):
    inventory_product_name = problem_logged_page.get_product_name(product)
    inventory_product_img_src = problem_logged_page.get_product_image_src(product)
    problem_logged_page.get_product_description(product)
    product_description_page = InventoryItemPage(page)
    product_description_page.is_loaded()
    product_description_name = product_description_page.get_product_name()
    product_description_img_src = product_description_page.get_image_src()
    assert inventory_product_img_src != product_description_img_src
    assert inventory_product_name != product_description_name

@pytest.mark.regression
def test_visual_user_img_problem(visual_user_logged_page, page: Page):
    inventory_product_img_src = visual_user_logged_page.get_product_image_src("Sauce Labs Backpack")
    visual_user_logged_page.get_product_description("Sauce Labs Backpack")
    product_description_page = InventoryItemPage(page)
    product_description_page.is_loaded()
    product_img_src = product_description_page.get_image_src()
    assert inventory_product_img_src != product_img_src

@pytest.mark.regression
@pytest.mark.parametrize("product", [("Sauce Labs Backpack"), ("Test.allTheThings() T-Shirt (Red)")])
def test_visual_user_price_problem(visual_user_logged_page, page: Page, product):
    product_price = visual_user_logged_page.get_product_price(product)
    visual_user_logged_page.get_product_description(product)
    product_description_page = InventoryItemPage(page)
    product_description_page.is_loaded()
    product_description_price = product_description_page.get_price()
    assert product_price != product_description_price

