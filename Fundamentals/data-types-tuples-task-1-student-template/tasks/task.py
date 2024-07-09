from typing import Tuple


def get_tuple(num: int) -> Tuple[int]:
    list_t = []
    num = str(num)
    for elm in num.strip(','):
        list_t.append(int(elm))
    return tuple(list_t)


print(get_tuple(87178291199))
print(get_tuple(6373))