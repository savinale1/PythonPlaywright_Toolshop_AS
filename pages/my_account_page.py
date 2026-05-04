from playwright.sync_api import Page
from pages.base_page import BasePage


class MyAccountPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "/account"
        self.sign_out_button = page.get_by_role("button", name="Sign out")

        # My Account navigation bar
        self.nav_items = {
            "favorites": page.locator("[data-test='nav-favorites']"),
            "profile": page.locator("[data-test='nav-profile']"),
            "invoices": page.locator("[data-test='nav-invoices']"),
            "messages": page.locator("[data-test='nav-messages']"),
        }

    def account_name(self, full_name: str):
        return self.page.get_by_text(full_name)

    def sign_out(self, account_name: str):
        self.page.get_by_role("button", name = account_name).click()
        self.sign_out_button.click()

    def open(self, base_url):
        self.goto(f'{base_url}{self.path}')

    # To handle navigation from My Account page to the Profile
    def go_to_profile(self):
        self.page.locator("[data-test='nav-profile']").click()

