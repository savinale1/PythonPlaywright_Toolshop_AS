import pytest
from pages.login_page import LoginPage
from config import get_browser_context_options, get_email, get_password
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def authenticated_context(browser):
    context = browser.new_context(**get_browser_context_options())
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.goto()
    login_page.authenticate(
        get_email(),
        get_password()
    )
    # optional: wait for login to complete
    page.wait_for_load_state("networkidle")
    yield context
    context.close()

@pytest.fixture(scope="function")
def authenticated_page(authenticated_context):
    page = authenticated_context.new_page()
    yield page
    page.close()