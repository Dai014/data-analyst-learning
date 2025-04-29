import logging

# Configure logging
logging.basicConfig(
    filename='app.log',  # Log file name
    level=logging.DEBUG,  # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message):
    logging.error(message)

def log_debug(message):
    logging.debug(message)

# Example usage
if __name__ == "__main__":
    log_info("Logging module initialized.")
    log_warning("This is a warning message.")
    log_error("This is an error message.")
    log_debug("This is a debug message.")