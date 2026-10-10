from playwright.sync_api import Page, expect


class InventoryItemPage():
    def __init__(self, page: Page):
        self.page = page
        self.product_description = self.page.locator("div.inventory_details_desc_container")
        self.product_price = self.product_description.locator("div.inventory_details_price")
        self.product_name = self.product_description.locator("div.inventory_details_name.large_size")
        self.img = self.page.locator("img.inventory_details_img")
        self.exit_button = page.get_by_role("button", name="Go back Back to products")

    def is_loaded(self):
        expect(self.exit_button).to_be_visible()

    def product_exists(self, product):
        expect(self.product_description.get_by_text(product).first).to_be_visible()

    def get_out(self):
        self.exit_button.click()

    def get_product_name(self):
        product_name = self.product_name.inner_text()
        return product_name

    def get_image_src(self):
        image_src = self.img.get_attribute("src")
        return image_src

    def get_price(self):
        price = self.product_price.inner_text()
        return float(price[1:])