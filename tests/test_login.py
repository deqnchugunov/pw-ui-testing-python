import pytest
from pages.login_page import LoginPage
from utils.constants import TestData, Locators

@pytest.mark.smoke
@pytest.mark.login
class TestLogin:
    """Login functionality tests"""
    
    def test_valid_login_success(self, page):
        """Test successful login with valid credentials"""
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.goto_login_page()
        
        # Perform login
        dashboard_page = login_page.login_as_valid_user()
        
        # Verify login success
        assert dashboard_page.is_dashboard_visible(), "Dashboard should be visible after successful login"
        assert "Welcome" in dashboard_page.get_welcome_message(), "Welcome message should be present"
        
        # Verify user is logged in
        assert dashboard_page.is_user_menu_visible(), "User menu should be visible"
    
    def test_invalid_login_failure(self, page):
        """Test login failure with invalid credentials"""
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.goto_login_page()
        
        # Attempt login with invalid credentials
        login_page.login_as_invalid_user()
        
        # Verify error message
        assert login_page.is_error_message_visible(), "Error message should be visible for invalid login"
        assert login_page.get_error_message() != "", "Error message should contain text"
    
    def test_empty_credentials_login(self, page):
        """Test login with empty credentials"""
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.goto_login_page()
        
        # Attempt login with empty credentials
        login_page.login("", "")
        
        # Verify error message
        assert login_page.is_error_message_visible(), "Error message should be visible for empty credentials"
    
    @pytest.mark.parametrize("username,password", [
        (TestData.VALID_USER["username"], ""),
        ("", TestData.VALID_USER["password"]),
        ("", ""),
    ])
    def test_login_with_empty_fields(self, page, username, password):
        """Test login with various empty field combinations"""
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.goto_login_page()
        
        # Attempt login
        login_page.login(username, password)
        
        # Verify error handling
        assert login_page.is_error_message_visible(), "Should show error for incomplete credentials"

    def test_login_page_elements_visibility(self, page):
        """Test that login page elements are visible"""
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.goto_login_page()
        
        # Verify elements are visible
        assert login_page.is_login_form_visible(), "Login form should be visible"
        assert login_page.is_element_visible(Locators.USERNAME_INPUT), "Username input should be visible"
        assert login_page.is_element_visible(Locators.PASSWORD_INPUT), "Password input should be visible"
        assert login_page.is_element_visible(Locators.SUBMIT_BUTTON), "Login button should be visible"