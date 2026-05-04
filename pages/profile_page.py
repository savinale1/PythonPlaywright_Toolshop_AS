from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.fld_first_name = page.locator("[data-test=\"first-name\"]")
        self.fld_last_name = page.locator("[data-test=\"last-name\"]")
        self.fld_email = page.locator("[data-test=\"email\"]")
        self.btn_update = page.locator("[data-test=\"update-profile-submit\"]")

    def open(self, base_url):
        self.page.goto(f"{base_url}/account/profile")

    def get_first_name(self):
        return self.fld_first_name.input_value()

    def get_last_name(self):
        return self.fld_last_name.input_value()

    def update_name(self, first_name: str, last_name: str):
        self.fld_first_name.fill(first_name)
        self.fld_last_name.fill(last_name)
        self.fld_last_name.press("Tab")
        self.btn_update.click()