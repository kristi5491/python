### OOP. Exceptions. Task 2
***
#### Description

Write a function `divide` which accepts a string that contains two integers, separated by **spaces** (integers can be separated by more than one space).
You have to perform the division operation (`a / b`) and return the result (float) or an error message.

The structure of the error message is the following: `Error code: {error message}`.

#### Example

    >>> divide("4 2")
    2.0

    >>> divide("4 0")
    "Error code: division by zero"

    >>> divide("* 1")
    "Error code: invalid literal for int() with base 10: '*'"
