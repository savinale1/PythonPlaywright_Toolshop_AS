from pages.login_page import LoginPage
from config import get_email, get_password

def test_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    email = get_email()
    password = get_password()
    page.pause()
    login_page.authenticate(email, password)

