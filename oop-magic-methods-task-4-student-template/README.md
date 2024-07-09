## Magic methods. Task 4
***
#### Description

You have to implement class `Book` with attributes `price, author, name.`

- `author` and `name` fields have to be immutable;
- `price` field may be changes but has to be in `0 <= price <= 100` range.

If user tries to change `author` or `name` fields after
initialization or set price out of range, the `ValueError` should be raised.

Implement descriptors `PriceControl` and `NameControl` to validate parameters.

#### Example

    >>> b = Book("William Faulkner", "The Sound and the Fury", 12)
    >>> print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
    Author='William Faulkner', Name='The Sound and the Fury', Price='12'
    
    >>> b.price = 55
    >>> b.price
    55
    >>> b.price = -12  # => ValueError: Price must be between 0 and 100.
    >>> b.price = 101  # => ValueError: Price must be between 0 and 100.
    
    >>> b.author = "new author"  # => ValueError: Author can not be changed.
    >>> b.name = "new name"      # => ValueError: Name can not be changed.

