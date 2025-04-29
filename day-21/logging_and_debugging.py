import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def debug_example_function(param):
    logging.debug(f"Function debug_example_function called with param: {param}")
    try:
        result = 10 / param
        logging.info(f"Result of division: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero.")
        return None
    except Exception as e:
        logging.exception("An unexpected error occurred.")
        return None

if __name__ == "__main__":
    logging.info("Starting the logging and debugging example.")
    debug_example_function(5)
    debug_example_function(0)  # This will trigger an error
    logging.info("Finished the logging and debugging example.")