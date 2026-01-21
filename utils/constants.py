class Locators:
    """Common locators used across pages"""
    
    # Common elements
    LOADING_SPINNER = ".loading-spinner"
    ALERT_MESSAGE = ".alert"
    ERROR_MESSAGE = ".error-message"
    
    # Buttons
    SUBMIT_BUTTON = "button[type='submit']"
    SAVE_BUTTON = "button:has-text('Save')"
    CANCEL_BUTTON = "button:has-text('Cancel')"
    DELETE_BUTTON = "button:has-text('Delete')"
    
    # Inputs
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    EMAIL_INPUT = "#email"
    SEARCH_INPUT = "[role='searchbox']"
    
    # Navigation
    NAVIGATION_MENU = ".navbar"
    USER_MENU = ".user-menu"
    LOGOUT_LINK = "a:has-text('Logout')"

class TestData:
    """Test data constants"""
    
    # User credentials
    VALID_USER = {
        "username": "testuser",
        "password": "password123"
    }
    
    INVALID_USER = {
        "username": "wronguser",
        "password": "wrongpass"
    }
    
    # Test data
    TEST_EMAIL = "test@example.com"
    TEST_NAME = "Test User"
    TEST_PHONE = "+1234567890"
    
    # URLs
    LOGIN_URL = "/login"
    DASHBOARD_URL = "/dashboard"
    ADMIN_URL = "/admin"

class TestConstants:
    """General test constants"""
    
    # Timeouts
    DEFAULT_TIMEOUT = 30000
    SHORT_TIMEOUT = 5000
    MEDIUM_TIMEOUT = 15000
    LONG_TIMEOUT = 30000
    
    # Wait states
    VISIBILITY_STATE = "visible"
    HIDDEN_STATE = "hidden"
    ENABLED_STATE = "enabled"
    DISABLED_STATE = "disabled"
    
    # Test tags
    SMOKE_TAG = "smoke"
    REGRESSION_TAG = "regression"
    INTEGRATION_TAG = "integration"