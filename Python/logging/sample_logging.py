import logging


def decorator_func(original_func):
    ## it is used to create log file with all logs
    logging.basicConfig(filename=f"logging/{original_func.__name__}.log", level=logging.INFO)

    def wrapper():
        logging.info(f"This is before : {original_func.__name__}")
        return original_func()
    
    return wrapper

@decorator_func
def display_info():
    print("This is display_info funtion")

display_info()