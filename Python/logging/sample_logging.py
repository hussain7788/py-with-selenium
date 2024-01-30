# import logging


# # def decorator_func(original_func):
# #     ## it is used to create log file with all logs
# #     logging.basicConfig(filename=f"logging/{original_func.__name__}.log", level=logging.INFO)

# #     def wrapper():
# #         logging.info(f"This is before : {original_func.__name__}")
# #         return original_func()
    
# #     return wrapper

# # @decorator_func
# # def display_info():
# #     print("This is display_info funtion")

# # display_info()


# # def decorator(func):
# #     logging.basicConfig(filename=f"logging/{func.__name__}.log", level=logging.INFO)
# #     def wrapper_func(*args, **kwargs):
# #         logging.info(f"This is before :{func.__name__}")
# #         print(args, kwargs)
# #         return func()
    
# #     return wrapper_func

# # @decorator
# # def test_func():
# #     print(f"This is main : {test_func.__name__}")


# # test_func()

# def sample():
#     print(sample.__name__)
# sample()


def test():
    import pdb;pdb.set_trace()
    import os, logging
    dir_name = os.path.dirname(__file__)
    logging.basicConfig(filename=os.path.join(dir_name, 'display_info.log'), level=logging.INFO)
    for i in range(1,10):
        logging.info(f"value {i}")
    
test()