import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Base URL configuration
    BASE_URL = os.getenv('BASE_URL', 'http://localhost:3000')
    
    # Browser configuration
    HEADLESS = os.getenv('HEADLESS', 'true').lower() == 'true'
    SLOW_MO = int(os.getenv('SLOW_MO', '0'))
    TIMEOUT = int(os.getenv('TIMEOUT', '30000'))
    
    # Viewport configuration
    VIEWPORT_WIDTH = int(os.getenv('VIEWPORT_WIDTH', '1280'))
    VIEWPORT_HEIGHT = int(os.getenv('VIEWPORT_HEIGHT', '720'))
    
    # Test configuration
    DEFAULT_TIMEOUT = int(os.getenv('DEFAULT_TIMEOUT', '30000'))
    RETRY_COUNT = int(os.getenv('RETRY_COUNT', '1'))
    
    # Reporting configuration
    REPORT_DIR = os.getenv('REPORT_DIR', 'reports')
    SCREENSHOT_DIR = os.getenv('SCREENSHOT_DIR', 'screenshots')
    
    # Environment configuration
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    
    @classmethod
    def get_browser_options(cls):
        options = {
            'headless': cls.HEADLESS,
            'slow_mo': cls.SLOW_MO,
            'timeout': cls.TIMEOUT,
            'viewport': {
                'width': cls.VIEWPORT_WIDTH,
                'height': cls.VIEWPORT_HEIGHT
            }
        }

        # Add environment-specific overrides
        if cls.ENVIRONMENT == 'staging':
            options['headless'] = True
        elif cls.ENVIRONMENT == 'production':
            options['headless'] = True

        return options
