from typing import List, Tuple


def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    new_list = []
    [new_list.append(elem) for elem in str_list if elem not in new_list]
    return sorted(new_list)


print(sort_unique_elements(('red', 'white', 'black', 'red', 'green', 'black')))
