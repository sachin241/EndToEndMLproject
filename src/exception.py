import sys


def error_message(error,error_detail) -> str:
    """Prints an error message to stderr and exits the program."""
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script: [{file_name}] | line number: [{exc_tb.tb_lineno}] | error message: [{error}]"
    return error_message
    sys.exit(1)
class CustomException(Exception):
    """Custom exception class that includes error details and system information."""
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message
        self.error_detail = error_detail

    def __str__(self):
        return f"Error message: {self.error_message} | Error detail: {self.error_detail}"