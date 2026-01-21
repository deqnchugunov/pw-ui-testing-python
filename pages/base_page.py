from playwright.sync_api import Page, Locator
from typing import Optional, Union
import time
from utils.logger import setup_logger

class BasePage:
    """Base page class with common functionality"""
    
    def __init__(self, page: Page):
        self.page = page
        self.logger = setup_logger(f"Page_{self.__class__.__name__}")
    
    def navigate_to(self, url: str):
        """Navigate to specified URL"""
        self.logger.info(f"Navigating to {url}")
        self.page.goto(url)
        return self
    
    def wait_for_load_state(self, state: str = "networkidle", timeout: int = 30000):
        """Wait for page load state"""
        self.logger.debug(f"Waiting for load state: {state}")
        self.page.wait_for_load_state(state, timeout=timeout)
        return self
    
    def wait_for_selector(self, selector: str, timeout: int = 30000):
        """Wait for selector to appear"""
        self.logger.debug(f"Waiting for selector: {selector}")
        return self.page.wait_for_selector(selector, timeout=timeout)
    
    def wait_for_element(self, locator: Union[Locator, str], timeout: int = 30000):
        """Wait for element to be visible"""
        if isinstance(locator, str):
            locator = self.page.locator(locator)
        self.logger.debug(f"Waiting for element: {locator}")
        locator.wait_for(timeout=timeout)
        return self
    
    def get_locator(self, selector: str) -> Locator:
        """Get locator by selector"""
        return self.page.locator(selector)
    
    def take_screenshot(self, path: str = None):
        """Take screenshot of current page"""
        if not path:
            timestamp = int(time.time())
            path = f"screenshots/screenshot_{timestamp}.png"
        
        self.page.screenshot(path=path)
        self.logger.info(f"Screenshot saved to {path}")
        return path
    
    def get_text_content(self, selector: str) -> str:
        """Get text content of element"""
        element = self.get_locator(selector)
        return element.text_content()
    
    def is_element_visible(self, selector: str, timeout: int = 5000) -> bool:
        """Check if element is visible"""
        try:
            self.wait_for_selector(selector, timeout=timeout)
            return True
        except Exception as e:
            self.logger.debug(f"Element not visible or error occurred: {e}")
            return False
    
    def scroll_to_element(self, selector: str):
        """Scroll to element"""
        element = self.get_locator(selector)
        element.scroll_into_view_if_needed()
        return self
    
    def wait_and_click(self, selector: str, timeout: int = 30000):
        """Wait for element and click it"""
        self.wait_for_element(selector, timeout)
        self.get_locator(selector).click()
        return self
    
    def wait_and_fill(self, selector: str, value: str, timeout: int = 30000):
        """Wait for input and fill it"""
        self.wait_for_element(selector, timeout)
        self.get_locator(selector).fill(value)
        return self
    
    def wait_and_clear(self, selector: str, timeout: int = 30000):
        """Wait for input and clear it"""
        self.wait_for_element(selector, timeout)
        self.get_locator(selector).clear()
        return self