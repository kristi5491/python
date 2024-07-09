### Functions. Decorators. Functions arguments. Task 1. 
***

We have a list of dictionaries:
```python
friends = [
    {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
    {'name': 'Emily', 'gender': 'female', 'sport': 'volleyball'},
]
```
Create functions `query`, `select`, `field_filter` to work with lists similar to 
`friends`.
Stubs for these functions are already created.

Example:
```python
>>> result = query(
    friends,
    select('name', 'gender', 'sport'),
    field_filter('sport', *('Basketball', 'volleyball')),
    field_filter('gender', *('male',)),
)
>>> result
[{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}]
```
These functions have to provide with possibility to select necessary columns
and make filtering by these columns

Do not forget the documentation for each function!
