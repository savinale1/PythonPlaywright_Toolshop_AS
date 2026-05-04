

# Created a new user, then logged in with those credentials to the account
# Verify that the user's name correctly displayed at the My Account page at nav bar
def test_user_successfully_logged_in(user_login, register_user):
    page = user_login
    assert page.get_by_text(f"{register_user.first_name} {register_user.last_name}").is_visible()




