from playwright.sync_api import Page, expect
class InventoryPage():
    def __init__(self, page: Page):
        self.page = page
        self.title = page.get_by_text("Products").first
        self.inventory_item = self.page.locator(".inventory_item")
        self.inventory_item_name = self.inventory_item.locator(".inventory_item_name")
        self.inventory_item_price = self.inventory_item.locator(".inventory_item_price")
        self.inventory_order_selector = self.page.locator("select.product_sort_container")
        self.img = self.page.locator(".inventory_item_img")
        self.shopping_cart_badge = self.page.locator("span.shopping_cart_badge")

    def is_loaded(self):
        expect(self.title).to_be_visible()

    def open(self):
        self.page.goto("/inventory.html")

    def shopping_cart_badge_is_visible(self):
        expect(self.shopping_cart_badge).to_be_visible()

    def shopping_cart_badge_is_not_visible(self):
        expect(self.shopping_cart_badge).not_to_be_visible()

    def get_product_card(self, product):
        product_card = self.inventory_item.filter(has_text=product)
        return product_card

    def add_to_cart(self, product):
        product_card = self.get_product_card(product)
        product_card.get_by_role("button", name="Add to cart").click()
        expect(product_card.get_by_role("button", name="Remove")).to_be_visible()

    def remove_from_cart(self, product):
        product_card = self.get_product_card(product)
        product_card.get_by_role("button", name="Remove").click()
        expect(product_card.get_by_role("button", name="Add to cart")).to_be_visible()

    def get_product_description(self, product):
        product_card = self.get_product_card(product)
        product_card.locator(".inventory_item_name").click()

    def open_cart(self):
        self.page.locator("a.shopping_cart_link").click()

    def order_inventory_name_az(self):
        self.inventory_order_selector.select_option("az")

    def order_inventory_name_za(self):
        self.inventory_order_selector.select_option("za")

    def order_inventory_price_lohi(self):
        self.inventory_order_selector.select_option("lohi")

    def order_inventory_price_hilo(self):
        self.inventory_order_selector.select_option("hilo")

    def get_list_of_titles(self):
        titles_list = self.inventory_item_name.all_inner_texts()
        return titles_list

    def get_list_of_prices(self):
        prices_list = self.inventory_item_price.all_inner_texts()
        return prices_list

    def get_src_list(self):
        images_list = self.img.evaluate_all("elements => elements.map(el => el.getAttribute('src'))")
        return images_list

    def get_product_image_src(self, product):
        image_src = self.inventory_item.filter(has_text=product).locator("img.inventory_item_img").get_attribute("src")
        return image_src

    def get_product_name(self, product):
        product_name = self.inventory_item_name.filter(has_text=product).inner_text()
        return product_name

    def get_product_price(self, product):
        product_item = self.inventory_item.filter(has_text=product)
        product_price = product_item.locator(".inventory_item_price").inner_text()
        return float(product_price[1:])