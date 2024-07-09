from typing import List, Tuple, Union

def seq_sum(sequence: Union[List, Tuple]) -> int:
    total = 0
    for element in sequence:
        if isinstance(element, (list, tuple)):
            total += seq_sum(element)
        else:
            total += element
    return total


sequence = [1, 2, 3, [4, 5, (6, 7)]]
print(seq_sum(sequence))
