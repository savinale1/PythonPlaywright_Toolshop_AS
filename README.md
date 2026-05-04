Playwright_Spring2026

Playwright test automation project for Tool Shop e-commerce site testing.

Setup
Clone the repository:
git clone https://github.com/savinale1/PythonPlaywright_Toolshop_AS.git

Install dependencies:
pip install -r requirements.txt

Install Playwright browsers:
playwright install

Running Tests
Run all tests:
pytest
Run specific test file:
pytest tests/test_login_logout.py
Run with verbose output:
pytest -vv
Run in headed mode (show browser):
pytest --headed



Project Structure
tests/               # Test files
pages/               # Page Object Model classes (e.g. LoginPage)
fixtures/            # Pytest fixtures (menu, new_user, extended_page)
forms/               # Form-related page objects (e.g. NavMenu)
conftest.py          # Pytest configuration + shared fixtures
config.py            # Central configuration
pytest.ini           # Pytest settings and markers
.env_example         # Template for environment variables
utils/helpers.py     # Helper functions
requirements.txt     # Dependencies