def decorator_fun(original_func):

    def wrapper_func(*args, **kwargs):
        print(f"This is before: {original_func.__name__}")
        return original_func(*args, **kwargs)
    return wrapper_func

# @decorator_fun
def display_func():
    print("This is display_func ")

# @decorator_fun
def sum_num(val1, val2):
    print("This is Sum of Nums:", val1+val2)

#### calling without decorator 
# display_func = decorator_fun(display_func)
# display_func()

# sum_num = decorator_fun(sum_num)
# sum_num(10, 20)
###############################3


@decorator_fun  # decorator
def display_func():
    print("This is display_func ")

## calling with decorator
display_func()    # it is same like above 


@decorator_fun  # decorator
def sum_num(val1, val2):
    print("This is Sum of Nums:", val1+val2)

display_func()  #it is same like above 

def deco_func(func):

    def wrapper_func():
        res = func()
        add = res+ 5
        return add
    return wrapper_func

@deco_func
def sample():
    return 10

print(sample())
