## Functions. Decorators. Decorators. Task 1.

***
Create a decorator function `time_decorator` which has to calculate decorated function execution time
and put this time value to `execution_time` dictionary where `key` is 
decorated function name and `value` is this function execution time.
For example:
```python
@time_decorator
def func_add(a, b):
    sleep(0.2)
    return a + b

>>> func_add(10, 20)
30

>>> execution_time['func_add']
0.212341254
```
