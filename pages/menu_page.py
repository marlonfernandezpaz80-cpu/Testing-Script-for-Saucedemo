from playwright.sync_api import Page, expect

class MenuPage():
    def __init__(self, page: Page):
        self.page = page
        self.menu_button = self.page.get_by_role("button", name="Open Menu")
        self.all_items_link = self.page.get_by_role("link", name="All items")
        self.logout_link = self.page.get_by_role("link", name="Logout")
        self.about_link = self.page.get_by_role("link",name="About")
        self.reset_app_state_link = self.page.get_by_role("link", name="Reset App State")
        self.close_menu_button = self.page.get_by_role("button", name="Close Menu")
        self.navigation_div = self.page.locator("div.bm-menu")

    def is_loaded(self):
        expect(self.navigation_div).to_be_visible()

    def is_not_loaded(self):
        expect(self.navigation_div).not_to_be_visible()

    def open_menu(self):
        self.menu_button.click()

    def close_menu(self):
        self.close_menu_button.click()

    def click_all_items(self):
        self.all_items_link.click()

    def click_logout(self):
        self.logout_link.click()

    def click_about(self):
        self.about_link.click()

    def click_reset_app_state(self):
        self.reset_app_state_link.click()