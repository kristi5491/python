from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    dict_num = {}
    for i in range (1, num + 1):
        dict_num[i] = i ** 2
    return dict_num


print(generate_squares(5))
