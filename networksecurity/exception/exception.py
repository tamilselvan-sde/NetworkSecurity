import sys
from networksecurity.logging.logger import logger  # ✅ Use logger instead of logging

class NetworkSecurityException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        self.error_message = str(error_message)  # Ensure error_message is a string
        _, _, exc_tb = error_detail.exc_info()
        
        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        return f"Error occurred in script: [{self.filename}] at line number: [{self.lineno}] error message: [{self.error_message}]"

if __name__ == "__main__":
    try:
        logger.info("Starting exception test...")  # ✅ Use logger instead of logging.log()
        a = 1 / 1  # This will cause a ZeroDivisionError
    except Exception as e:
        logger.error("An error occurred", exc_info=True)  # ✅ Log the exception
        raise NetworkSecurityException(e, sys)
