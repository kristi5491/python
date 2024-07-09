from typing import Any, Tuple, List


def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    if len(lst) < 2:
        return []
    new_list = []
    a = lst[0]
    b = lst[1]
    for numbers in range(1, len(lst)):
        b = lst[numbers]
        new_list.append((a, b))
        a = b
    return new_list


print(get_pairs([1, 2, 3, 8, 9]))