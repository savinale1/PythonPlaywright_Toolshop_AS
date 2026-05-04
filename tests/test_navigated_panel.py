import pytest
from pages.forms.navigated_panel import NavMenu


@pytest.mark.usefixtures("page")
def test_open_hand_tools(page, base_url):
    page.goto(base_url)  # replace with real URL
    nav = NavMenu(page)
    page.pause()

    nav.btn_contact.click()
    assert page.url != base_url

