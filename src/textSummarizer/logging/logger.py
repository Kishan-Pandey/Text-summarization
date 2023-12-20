# my_project/logging/custom_logger.py

import logging

def get_logger():
    # Create a custom logger named 'logger'
    logger = logging.getLogger('logger')

    # Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a console handler and set the formatter
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)
    logger.info()
    # You can add more handlers or customize the logger further if needed

    return logger
