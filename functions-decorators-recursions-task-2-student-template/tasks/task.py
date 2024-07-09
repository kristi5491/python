from typing import Any, List


def linear_seq(sequence: List[Any]) -> List[Any]:
    total_mus = []
    for elem in sequence:
        if isinstance(elem, (list, tuple)):
            total_mus.extend(linear_seq(list(
                elem)))
        else:
            total_mus.append(elem)
    return total_mus


sequence = [1, 2, 3, [4, 5, (6, 7)]]
print(linear_seq(sequence))
