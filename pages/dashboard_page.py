from pages.base_page import BasePage
from utils.constants import Locators
from playwright.sync_api import Page

class DashboardPage(BasePage):
    """Dashboard page implementation"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_message = self.get_locator(".welcome-message")
        self.user_menu = self.get_locator(Locators.USER_MENU)
        self.logout_link = self.get_locator(Locators.LOGOUT_LINK)
    
    def is_dashboard_visible(self) -> bool:
        """Check if dashboard is visible"""
        return self.is_element_visible(".welcome-message")
    
    def get_welcome_message(self) -> str:
        """Get welcome message text"""
        return self.get_text_content(".welcome-message")
    
    def logout(self):
        """Logout from dashboard"""
        self.wait_and_click(Locators.USER_MENU)
        self.wait_and_click(Locators.LOGOUT_LINK)
        # Import locally to avoid circular import
        from pages.login_page import LoginPage
        return LoginPage(self.page)
    
    def is_user_menu_visible(self) -> bool:
        """Check if user menu is visible"""
        return self.is_element_visible(Locators.USER_MENU)
    
    def wait_for_dashboard_load(self) -> "DashboardPage":
        """Wait for dashboard to fully load"""
        self.wait_for_load_state()
        self.wait_for_element(".welcome-message")
        return self