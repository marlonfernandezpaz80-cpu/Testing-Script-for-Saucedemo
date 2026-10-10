from playwright.sync_api import Page, expect

class CheckoutPage():
    def __init__(self, page: Page):
        self.page = page
        self.cancel_button = self.page.get_by_role("button", name="Go back Cancel")
        self.continue_button = self.page.get_by_role("button", name="Continue")
        self.finish_button = self.page.get_by_role("button", name="Finish")
        self.back_home_button = self.page.get_by_role("button", name="Back Home")
        self.generate_pdf_button = self.page.get_by_role("button", name="Generate PDF order")
        self.item_total = self.page.locator("div.summary_subtotal_label")
        self.tax = self.page.locator("div.summary_tax_label")
        self.total = self.page.locator("div.summary_total_label")

    def step_one_is_loaded(self):
        expect(self.page).to_have_url("/checkout-step-one.html")

    def step_two_is_loaded(self):
        expect(self.page).to_have_url("/checkout-step-two.html")

    def step_three_is_loaded(self):
        expect(self.page).to_have_url("/checkout-complete.html")

    def fill_user_form(self, name, last_name, postal_code):
        self.fill_first_name(name)
        self.fill_last_name(last_name)
        self.fill_postal_code(postal_code)

    def back_home(self):
        self.back_home_button.click()

    def generate_pdf(self):
        self.generate_pdf_button.click()
        expect(self.page.get_by_text("Thank you for your order!").first).to_be_visible()
    
    def fill_first_name(self, first_name):
        self.page.get_by_role("textbox", name="First Name").fill(first_name)

    def fill_last_name(self, last_name):
        self.page.get_by_role("textbox", name="Last Name").fill(last_name)

    def fill_postal_code(self, postal_code):
        self.page.get_by_role("textbox", name="Zip/Postal Code").fill(postal_code)

    def get_subtotal_price(self):
        subtotal = self.item_total.inner_text().replace("Item total: $", "")
        subtotal = float(subtotal)
        return subtotal

    def get_tax(self):
        tax = self.tax.inner_text().replace("Tax: $", "")
        tax = float(tax)
        return tax

    def get_total_price(self):
        total_price = self.total.inner_text().replace("Total: $", "")
        total_price = float(total_price)
        return total_price

    def click_continue(self):
        self.continue_button.click()

    def click_finish (self):
        self.finish_button.click()

