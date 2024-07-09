from typing import Tuple, Union
from math import sqrt


def solution(a, b, c) -> Union[Tuple[float, float], Tuple[float], None]:
    result = None
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        result = (-b - sqrt(discriminant))//(2 * a), (-b + sqrt(discriminant))//(2 * a)
    if discriminant == 0:
        result = -b/(2 * a),
    print(result)
    return result

my_tuple = (1,1,2,3,4)
my_set = {1,1,2}
my_dict = {
    "name": 'khyrystyna',
    "last_name":'savchyn',
    "last_name":["savchyn","savchyn"]
}
print(my_tuple)
if __name__ == "__main__":
    assert solution(1, 6, 5) == (-5, -1)
    assert solution(1, 4, 4) == (-2,)
    assert solution(1, 6, 45) is None
    print(my_set)
    print(my_tuple)
    print(my_dict)
    print(id(my_tuple))