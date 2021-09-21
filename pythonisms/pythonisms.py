from functools import wraps


def invocation_log(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        print(f'Before Calling {func.__name__}')
        func(*args, **kwargs)
        print(f'After Calling {func.__name__}')

    return inner_func


@invocation_log
def say_hello(name):
    """Say hello to someone"""
    print(f"Hello, {name}!")
   
@mydeco
def add(a, b):
    return a + b
@mydeco
def mysum(*args):
    
    total = 0
    for one_item in args:
        total += one_item
    return total