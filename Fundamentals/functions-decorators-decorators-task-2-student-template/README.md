## Functions. Decorators. Decorators. Task 2

Write a decorator which logs information about calls of decorated function,
values of its arguments, values of keyword arguments and execution time. Log
should be written to a file.

### Example of using
``` python
@log
def foo(a, b, c):
    ...

foo(1, 2, c=3)
```

### log.txt
```
...
foo; args: a=1, b=2; kwargs: c=3; execution time: 0.12 sec.
...
```
