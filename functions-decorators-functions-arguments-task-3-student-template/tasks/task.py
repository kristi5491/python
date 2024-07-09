from typing import List, Dict


def combine_dicts(*args: List[Dict[str, int]]) -> Dict[str, int]:
    new_dict = {}
    for diction in args:
        for key, value in diction.items():
                if key not in new_dict:
                    new_dict[key] = value
                else:
                    new_dict[key] += value
    return new_dict


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
print(combine_dicts(dict_1, dict_2))
