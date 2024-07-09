### Magic Methods. Task 1
***
#### Description

You have to overload the addition operator in `Counter` class. Use the `__add__()` magic method to overload the addition.

For example, in case of *a + b*, *a* object should have `__add__()` which accepts *b* as a second parameter (`self` goes first).

In this case, `Counter` object accepts a list from int as a parameter. Object to summarize with will be a str object.
The result should be a list of strings which have the following pattern: `1 test` - one object from list and str separated by the whitespace.

#### Example

    >>> Counter([1, 2, 3]) + "mississippi"

    ["1 mississippi", "2 mississippi" , "3 mississippi"]
