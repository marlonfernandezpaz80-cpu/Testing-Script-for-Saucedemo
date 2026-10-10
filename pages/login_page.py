from playwright.sync_api import Page, expect
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.input_username = self.page.get_by_placeholder("Username")
        self.input_password = self.page.get_by_placeholder("Password")
        self.login_button = self.page.get_by_role("button", name="Login")
        self.login_error_sign = self.page.locator("[data-test='error']").filter(has_text="do not match")
        self.login_empty_box_sign = self.page.locator("[data-test='error']").filter(has_text="is required")
        self.login_locked_out_sign = self.page.locator("[data-test='error']").filter(has_text="user has been locked out")
    def open(self):
        self.page.goto("/")

    def login(self, username, password):
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.login_button.click()

    def is_loaded(self):
        expect(self.login_button).to_be_visible()