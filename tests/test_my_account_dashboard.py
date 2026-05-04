import pytest

from conftest import base_url
from pages.my_account_page import MyAccountPage


# Verify that the name of the user corresponds at the My Account page
def test_account_name_visible(my_account_page, register_user, user_login, base_url):
    page = user_login
    full_name = f"{register_user.first_name} {register_user.last_name}"
    assert my_account_page.account_name(full_name).is_visible()


# def test_account_navigation_bar_visible(my_account_page, register_user, user_login, base_url):
#     page = user_login
#     page.pause()
#     assert my_account_page.btn_favorites.is_visible()

@pytest.mark.parametrize("nav_item", [
    "favorites",
    "profile",
    "invoices",
    "messages"], ids=["Favorites", "Profile", "Invoices", "Messages"])

# For now, it opens the login page every time,
# Will use Parametrize approach for better options later
def test_account_navigation_bar_visible(my_account_page, user_login, register_user, base_url, nav_item):
    assert my_account_page.nav_items[nav_item].is_visible()