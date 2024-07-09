from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    """
    Returns the result of dividing two numbers or an error message.
    :arg
        str_with_ints: str, ex. "4 2";
    :return
        result of dividing: float, ex. 2.0 (4 / 2 = 2.0);
        error response in "Error code: {error message}: str;
    """
    try:
        num1, num2 = map(int, str_with_ints.strip().split())
        try:
            result = num1 / num2
            return result
        except ZeroDivisionError:
            return 'Error code: division by zero'
    except ValueError as e:
        return f"Error code: {str(e)}"


print(divide("4 2"))

print(divide("4 0"))

print(divide("* 1"))