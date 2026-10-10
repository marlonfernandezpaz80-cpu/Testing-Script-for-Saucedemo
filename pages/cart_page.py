from playwright.sync_api import Page, expect

class CartPage():
    def __init__(self, page: Page):
        self.page = page
        self.cart_item = self.page.locator("div.cart_item")
        self.prices = self.cart_item.locator("div.inventory_item_price")
        self.exit_button = self.page.get_by_role("button", name="Go back Continue Shopping")
        

    def open(self):
        self.page.goto("/cart.html")

    def is_loaded(self):
        expect(self.page.get_by_text("Your cart").first).to_be_visible()

    def get_out(self):
        self.exit_button.click()

    def remove_from_cart(self, product):
        target_cart_item = self.cart_item.filter(has_text=product)
        target_cart_item.get_by_role("button", name="Remove").click()
        expect(target_cart_item).not_to_be_visible()

    def get_product_card(self, product):
        product_card = self.cart_item.filter(has_text=product)
        return product_card

    def get_product_description(self, product):
        product_card = self.get_product_card(product)
        product_card.locator("div.inventory_item_name").click()

    def get_prices_list(self):
        prices_list = self.prices.all_inner_texts()
        formated_prices_list = []
        for price in prices_list:
            formated_prices_list.append(float(price[1:]))
        return formated_prices_list

    def product_exists(self, product):
        expect(self.cart_item.filter(has_text=product)).to_be_visible()

    def product_do_not_exists(self, product):
        expect(self.cart_item.filter(has_text=product)).not_to_be_visible()
    
    def checkout(self):
        self.page.get_by_role("button", name="Checkout").click()

    def products_are_not_visible(self):
        expect(self.cart_item).not_to_be_visible()

    