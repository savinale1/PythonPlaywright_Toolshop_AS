from playwright.sync_api import expect
from fixtures.api_fixtures import api_user_login

# this test doesn't work, because I was unable to get payload for api calls
def test_api_user_login(page, api_user_login):
    token = api_user_login["token"]
    print("TOKEN:", token)
    # verify UI
    page.goto("/account")
    expect(page.get_by_role("heading", name="My account")).to_be_visible()