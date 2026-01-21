from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from utils.constants import Locators, TestData
from playwright.sync_api import Page

class LoginPage(BasePage):
    """Login page implementation"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = self.get_locator(Locators.USERNAME_INPUT)
        self.password_input = self.get_locator(Locators.PASSWORD_INPUT)
        self.login_button = self.get_locator(Locators.SUBMIT_BUTTON)
        self.error_message = self.get_locator(Locators.ERROR_MESSAGE)
    
    def login(self, username: str, password: str) -> DashboardPage:
        """Perform login with credentials"""
        self.logger.info(f"Attempting login with user: {username}")
        
        # Fill credentials
        self.wait_and_fill(Locators.USERNAME_INPUT, username)
        self.wait_and_fill(Locators.PASSWORD_INPUT, password)
        
        # Click login button
        self.wait_and_click(Locators.SUBMIT_BUTTON)
        
        # Wait for navigation to dashboard
        self.wait_for_load_state()
        
        return DashboardPage(self.page)
    
    def login_as_valid_user(self) -> DashboardPage:
        """Login with valid test credentials"""
        return self.login(TestData.VALID_USER["username"], TestData.VALID_USER["password"])
    
    def login_as_invalid_user(self) -> "LoginPage":
        """Attempt login with invalid credentials"""
        self.login(TestData.INVALID_USER["username"], TestData.INVALID_USER["password"])
        return self
    
    def get_error_message(self) -> str:
        """Get error message text"""
        if self.is_element_visible(Locators.ERROR_MESSAGE):
            return self.get_text_content(Locators.ERROR_MESSAGE)
        return ""
    
    def is_login_form_visible(self) -> bool:
        """Check if login form is visible"""
        return self.is_element_visible(Locators.USERNAME_INPUT)
    
    def is_error_message_visible(self) -> bool:
        """Check if error message is visible"""
        return self.is_element_visible(Locators.ERROR_MESSAGE)
    
    def goto_login_page(self) -> "LoginPage":
        """Navigate to login page"""
        self.navigate_to("/login")
        return self