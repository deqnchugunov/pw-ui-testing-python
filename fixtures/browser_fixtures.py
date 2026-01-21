import pytest
from playwright.sync_api import sync_playwright
from utils.config import Config

@pytest.fixture(scope="session")
def browser_context():
    """Create browser context for all tests in session"""
    with sync_playwright() as p:
        browser = p.chromium.launch(**Config.get_browser_options())
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def page(browser_context):
    """Create page for each test function"""
    page = browser_context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def browser(browser_context):
    """Provide browser instance"""
    # Extract browser from context
    # This is a workaround since we don't have direct access to browser
    # But we can still provide the context which has the browser
    yield browser_context