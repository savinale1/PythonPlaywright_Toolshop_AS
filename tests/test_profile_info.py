import time

from pages.profile_page import ProfilePage


def test_profile_name_matches_user(user_login, register_user, my_account_page, profile_page, base_url):
    page = user_login
    page.goto(f"{base_url}/account")
    my_account_page.go_to_profile()
    page.pause()
    assert profile_page.get_first_name() == register_user.first_name, "First Name does not match"
    assert profile_page.get_last_name() == register_user.last_name, "Last Name does not match"

# This test requires more modification to handle the speed
# When it's slow there is no issue to update data
def test_update_profile_name(user_login, register_user, my_account_page, profile_page, base_url):
    page = user_login
    page.goto(f"{base_url}/account")
    my_account_page.go_to_profile()
    page.wait_for_load_state("networkidle")
    new_first = "UpdatedFirst"
    new_last = "UpdatedLast"

    # profile_page.fld_first_name.fill(new_first)
    # profile_page.fld_last_name.fill(new_last)
    # page.wait_for_load_state("networkidle")
    # profile_page.fld_email.click()
    # profile_page.btn_update.click()

    profile_page.update_name(new_first, new_last)
    page.reload()

    assert profile_page.get_first_name() == new_first
    assert profile_page.get_last_name() == new_last

# Test with API fixtures
# Need to work on this test
def test_profile_name(api_login, base_url, user_login):
    user = api_login["user"]


    for _ in range(5):
        first = profile_page.get_first_name()
        print(f"first {first}")
        print(f"user first name {user.first_name}")

        last = profile_page.get_last_name()
        print(f"last {last}")
        print(f"user last name {user.last_name}")

        page.pause()
        if first == user.first_name and last == user.last_name:
            break
        time.sleep(1)
        page.reload()

    assert first == user.first_name
    assert last == user.last_name