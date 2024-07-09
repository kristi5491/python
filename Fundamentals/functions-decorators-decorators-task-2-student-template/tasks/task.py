import time
from functools import wraps

def log(fn):
    """
    Add your code here or call it from here   
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        items = ['a','b','c']
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        exc_time = end_time - start_time
        kwarg_str = ', '.join([f'{k}={v}' for k, v in kwargs.items()])
        arg_str = ', '.join([f'{items[i]}={v}' for i, v in enumerate(args)])
        if len(kwargs) != 0:
            log_str = f"{fn.__name__}; args: {arg_str}; kwargs: {kwarg_str}; execution time: {exc_time:.2f} sec.\n"
        else:
            log_str = f"{fn.__name__}; args: {arg_str}; execution time: {exc_time:.2f} sec.\n"
        with open('data.txt', 'a') as file:
            file.write(log_str)
        return result

    return wrapper


@log
def foo(*args, **kwargs):
    time.sleep(0.1)
    args_sum = sum(args)
    kwargs_sum = sum(kwargs.values())
    total_sum = args_sum + kwargs_sum
    return total_sum


print(foo(1, 2, c=3))
print(foo(3, 2, c=1, d=5))
print(foo(3, 2, 4))