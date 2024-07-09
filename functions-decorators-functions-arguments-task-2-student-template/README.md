### Functions. Decorators. Functions arguments. Task 2. 
***
Create generic `union` and `intersect` functions to work with sets.
The functions must accept an arbitrary number of arguments of different types: `list`, `tuple`, `set`.
Each function must return value of `set` type.
For example:
```python
>>> union(('S', 'A', 'M'), ['S', 'P', 'A', 'C'])
{'S', 'P', 'A', 'M', 'C'}

>>> intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C'))
{'S', 'C'}
```
