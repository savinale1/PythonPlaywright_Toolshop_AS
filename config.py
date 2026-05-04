import os
from dotenv import load_dotenv
load_dotenv()

def get_base_url():
    return os.getenv('BASE_URL').lower()

def get_api_base_url():
    return os.getenv('API_BASE_URL').lower()

def get_user_agent():
    return os.getenv('USER_AGENT')

def get_browser():
    return os.getenv("BROWSER", "chromium").lower()

def is_headless():
    return os.getenv("HEADLESS", "false").lower() == "true"

def get_browser_launch_options():
    return {
        "headless": is_headless()
    }

def get_browser_context_options():
    return {
        "viewport": {
            "width": int(os.getenv("VIEWPORT_WIDTH", 1280)),
            "height": int(os.getenv("VIEWPORT_HEIGHT", 800)),
        }
    }

# User credentials Option #1
def get_user_info():
    return {
        "USER_FIRST_NAME" : os.getenv("USER_FIRST_NAME"),
        "USER_LAST_NAME" : os.getenv("USER_LAST_NAME"),
        "DATE_OF_BIRTH" : os.getenv("DATE_OF_BIRTH"),
        "COUNTRY" : os.getenv("COUNTRY"),
        "POSTAL_CODE" : os.getenv("POSTAL_CODE"),
        "STREET" : os.getenv("STREET"),
        "HOUSE_NUMBER" : os.getenv("HOUSE_NUMBER"),
        "CITY" : os.getenv("CITY"),
        "STATE" : os.getenv("STATE"),
        "PHONE" : os.getenv("PHONE"),
        "EMAIL" : os.getenv("EMAIL"),
        "PASSWORD" : os.getenv("PASSWORD")
    }

# Not sure which option I will leave
# User credentials Option #2
def get_user_first_name():
    return os.getenv("USER_FIRST_NAME")

def get_user_last_name():
    return os.getenv("USER_LAST_NAME")

def get_date_of_birth():
    return os.getenv("DATE_OF_BIRTH")

def get_country():
    return os.getenv("COUNTRY")

def get_postal_code():
    return os.getenv("POSTAL_CODE")

def get_street():
    return os.getenv("STREET")

def get_house_number():
    return os.getenv("HOUSE_NUMBER")

def get_city():
    return os.getenv("CITY")

def get_state():
    return os.getenv("STATE")

def get_phone():
    return os.getenv("PHONE")

def get_email():
    return os.getenv("EMAIL")

def get_password():
    return os.getenv("PASSWORD")