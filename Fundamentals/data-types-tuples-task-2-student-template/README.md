# Data Types. Tuples. Task 2

Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
of tuples containing pairs of elements. The pairs should be formed as in the
example. If there is only one element in the list, return `[]` instead.

__Example:__
```python
>>> get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]
>>> get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')] 
>>> get_pairs([1])
[]
```
