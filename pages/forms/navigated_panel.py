

class NavMenu:
    def __init__(self, page):
        self.page = page

        self.btn_home = page.locator("[data-test=\"nav-home\"]")
        self.btn_categories = page.locator("[data-test=\"nav-categories\"]")
        self.btn_contact = page.locator("[data-test=\"nav-contact\"]")
        self.btn_sign_in = page.locator("text=Sign in")
        self.btn_language = page.locator("text=EN")

        # User logged in - My Account menu available
        # Under {Fist_name Last_name} account btn
        self.btn_sign_out = page.get_by_role("button", name="Sign out")
        self.btn_my_account = page.locator("My account")
        self.btn_my_favorites = page.locator("My favorites")
        self.btn_my_profile = page.locator("My profile")
        self.btn_my_invoices = page.locator("My invoices")
        self.btn_my_messages = page.locator("My messages")

        # Under Categories btn there are dropdown items
        # Need more time to find locators for those elements
        self.btn_hand_tools = page.locator("text=Hand tools")
        self.btn_power_tools = page.locator("text=Power Tools")
        self.btn_other = page.locator("text=Other")
        self.btn_special_tools = page.locator("text=Special Tools")
        self.btn_rentals = page.locator("text=Rentals")

    # Need more time to implement the function which get user's name and last name and
    # implement it in searching the btn with it


    def go_home(self):
        self.btn_home.click()

    def open_categories(self):
        self.btn_categories.click()

    def open_contact(self):
        self.btn_contact.click()

    def sign_in(self):
        self.btn_sign_in.click()

    def select_language(self):
        self.btn_language.click()

    def open_hand_tools(self):
        self.btn_categories.click()
        self.btn_hand_tools.click()