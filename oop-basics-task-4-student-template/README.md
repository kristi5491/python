## OOP Basics. Task 4

Implement a custom dictionary that will memorize the 5 latest changed keys.
Using method "get_history" return these keys.

Example:
```python
>>> d = HistoryDict({"foo": 42})
>>> d.set_value("bar", 43)
>>> d.get_history()

["bar"]
```

*After your own implementation of the class have a look at collections.deque https://docs.python.org/3/library/collections.html#collections.deque*
