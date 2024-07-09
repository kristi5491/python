# Data Types. Lists. Task 3

Implement a function `foo(List[int]) -> List[int]` which, given a list of
integers, returns a new list such that each element at index `i` of the new list
is the product of all the numbers in the original array except the one at `i`.

__Example:__
```python
>>> foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]
>>>foo([3, 2, 1])
[2, 3, 6]
```
