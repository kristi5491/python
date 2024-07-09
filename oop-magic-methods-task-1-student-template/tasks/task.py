from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values
    # TODO: add your code here

    def __add__(self, other):
        array = []
        if not isinstance(other, str):
            raise TypeError("Can only add a string to Counter")
        for val in self.values:
            array.append(f'{val} {other}')
        return array


c = Counter([1, 2, 3]) + "mississippi"
print(c)