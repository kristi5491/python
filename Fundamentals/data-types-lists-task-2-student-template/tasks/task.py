from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    list_n = []
    for elem in range(1, n+1):
        if elem % 3 == 0 and elem % 5 == 0:
            list_n.append('FizzBuzz')
        elif elem % 3 == 0:
            list_n.append('Fizz')
        elif elem % 5 == 0:
            list_n.append('Buzz')
        else: list_n.append(elem)
    return list_n


print(get_fizzbuzz_list(5))
print(get_fizzbuzz_list(15))
print(get_fizzbuzz_list(27))
