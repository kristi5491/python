from typing import List


def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    multiplication_list = []
    new_list = []
    for num1 in range(row_start, row_end + 1):
        for num2 in range(column_start, column_end + 1):
            result = num1 * num2
            new_list.append(result)
        if not len(new_list) < (column_end - column_start + 1):
            multiplication_list.append(new_list.copy())
            new_list.clear()
    return multiplication_list


print(check(2, 4, 3, 7))
