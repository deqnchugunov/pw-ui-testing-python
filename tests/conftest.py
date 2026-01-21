import pytest
from playwright.sync_api import sync_playwright
from utils.config import Config
from utils.logger import setup_logger
import os

# Setup logging
test_logger = setup_logger("test_runner")

@pytest.fixture(scope="session")
def browser_context():
    """Create browser context for all tests in session"""
    test_logger.info("Setting up browser context")
    
    with sync_playwright() as p:
        # Launch browser with configured options
        browser = p.chromium.launch(**Config.get_browser_options())
        context = browser.new_context()
        
        # Set viewport
        context.set_viewport_size(Config.get_browser_options()['viewport'])
        
        yield context
        
        # Cleanup
        context.close()
        browser.close()
        test_logger.info("Browser context closed")

@pytest.fixture(scope="function")
def page(browser_context):
    """Create page for each test function"""
    test_logger.info("Creating new page for test")
    page = browser_context.new_page()
    
    # Set up page logging
    page.on("console", lambda msg: test_logger.info(f"[Console] {msg.text}"))
    page.on("request", lambda req: test_logger.debug(f"[Request] {req.method} {req.url}"))
    page.on("response", lambda resp: test_logger.debug(f"[Response] {resp.status} {resp.url}"))
    
    yield page
    
    # Cleanup page
    page.close()
    test_logger.info("Page closed")

@pytest.fixture(scope="function", autouse=True)
def test_setup_and_teardown(request, page):
    """Setup and teardown for each test"""
    test_logger.info(f"Starting test: {request.node.name}")
    
    # Setup - navigate to base URL
    page.goto(Config.BASE_URL)
    
    yield page
    
    # Teardown - take screenshot on failure
    if request.node.rep_call.failed:
        try:
            screenshot_path = f"screenshots/{request.node.name}_failed.png"
            page.screenshot(path=screenshot_path, full_page=True)
            test_logger.error(f"Screenshot saved for failed test: {screenshot_path}")
        except Exception as e:
            test_logger.error(f"Failed to save screenshot: {e}")
            # Continue execution even if screenshot fails

# Add pytest hook for better reporting
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Add custom report information"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)