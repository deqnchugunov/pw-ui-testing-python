import logging
import os
from datetime import datetime

def setup_logger(name, log_file=None, level=logging.INFO):
    """Setup logger with file and console handlers"""
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Prevent adding handlers multiple times
    if not logger.handlers:
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # File handler
        if log_file:
            # Ensure log directory exists
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
            
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
    
    return logger

def get_test_logger(test_name):
    """Get logger for specific test"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"logs/test_{test_name}_{timestamp}.log"
    return setup_logger(f"test_{test_name}", log_file)