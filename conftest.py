import requests

import config

import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.profile_page import ProfilePage
from utils.helpers import generate_user_registration_data, generate_address_data

@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Controls browser launch (headless, etc.)"""
    return config.get_browser_launch_options()

@pytest.fixture(scope="session")
def browser_context_args():
    """Controls browser context (viewport, etc.)"""
    return config.get_browser_context_options()

@pytest.fixture(scope="session")
def base_url():
    return config.get_base_url()

@pytest.fixture(scope="session")
def api_base_url():
    return config.get_api_base_url()

# Fixture to generate a new data for a user and
# then to register a new user in UI
# I will split into two fixtures in a future

# separate two fixtures
# Created data for the new user
@pytest.fixture(scope="session")
def test_user():
    user = generate_user_registration_data()
    user.address = generate_address_data()
    return user

# Register a new user
@pytest.fixture(scope="session")
def register_user(browser, base_url, test_user):
    context = browser.new_context()
    page = context.new_page()

    # page.goto("https://practicesoftwaretesting.com/auth/register")
    page.goto(f"{base_url}/auth/register")
    # couldn't fix to use base_url
    # page.goto("/auth/register")

    page.locator("[data-test=\"first-name\"]").fill(test_user.first_name)
    page.locator("[data-test=\"last-name\"]").fill(test_user.last_name)
    page.locator("[data-test=\"dob\"]").fill(test_user.birth_date)

    page.locator("[data-test=\"country\"]").select_option(test_user.address.country)
    page.locator("[data-test=\"postal_code\"]").fill(test_user.address.zip)
    page.locator("[data-test=\"house_number\"]").fill(test_user.address.building)
    page.locator("[data-test=\"street\"]").fill(test_user.address.street)
    page.locator("[data-test=\"city\"]").fill(test_user.address.city)
    page.locator("[data-test=\"state\"]").fill(test_user.address.state)

    page.locator("[data-test=\"phone\"]").fill(test_user.phone_number)
    page.locator("[data-test=\"email\"]").fill(test_user.email)
    page.locator("[data-test=\"password\"]").fill(test_user.password)

    print(test_user.email, test_user.password)

    page.locator("[data-test=\"register-submit\"]").click()
    # page.wait_for_timeout(1000)
    page.wait_for_load_state("networkidle")
    page.wait_for_url("**/auth/login")
    print("user has been created successfully")

    context.close()

    return test_user


# Use a test_user to log in
@pytest.fixture
def user_login(page, register_user):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.authenticate(
        register_user.email,
        register_user.password
    )
    page.wait_for_load_state("networkidle")
    return page

@pytest.fixture
def my_account_page(page):
    return MyAccountPage(page)

@pytest.fixture
def profile_page(page):
    return ProfilePage(page)

# For api use
@pytest.fixture
def api_profile_page(api_authenticated_page):
    return ProfilePage(api_authenticated_page)

# Required for using API
@pytest.fixture
def api_authenticated_page(browser, api_login):
    context = browser.new_context()
    context.add_cookies([{
        "name": "Authorization",
        "value": f"Bearer {api_login['token']}",
        "domain": "practicesoftwaretesting.com",
        "path": "/",
    }])
    page = context.new_page()
    yield page
    context.close()

# API Fixtures: api_user and api_login
@pytest.fixture(scope="session")
def api_user(api_base_url):
    user = generate_user_registration_data()
    user.address = generate_address_data()

    payload = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "address": {
            "street": user.address.street,
            "house_number": user.address.building,
            "city": user.address.city,
            "state": user.address.state,
            "country": user.address.country,
            "postal_code": user.address.zip,
        },
        "phone": user.phone_number,
        "dob": user.birth_date,
        "password": user.password,
        "email": user.email,
    }

    response = requests.post(f"{api_base_url}/users/register", json=payload)
    assert response.status_code in (200, 201)
    return user

@pytest.fixture(scope="session")
def api_login(api_base_url, api_user):
    payload = {
        "email": api_user.email,
        "password": api_user.password
    }
    response = requests.post(f"{api_base_url}/users/login", json=payload)

    print(response.status_code)
    print(response.text)

    assert response.status_code == 200

    token = response.json()["access_token"]
    return {
        "token": token,
        "user": api_user
    }


# @pytest.fixture(scope="session")
# def browser_type_launch_args() -> dict:
#     """Browser launch args from centralized config."""
#     return config.get_browser_context_options()
#
# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         'viewport': {
#             'width': config.get_browser_context_options()['viewport']['width'],
#             'height': config.get_browser_context_options()['viewport']['height'],
#         }
#     }
#
# @pytest.fixture(scope="session")
# def base_url() -> str:
#     return config.get_base_url()