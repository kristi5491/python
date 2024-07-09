from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    new_dict = {}
    s = s.lower()
    for char in s.strip(','):
        count_char = s.count(char)
        new_dict[char] = count_char
    return new_dict

result = 20 / 5 + 10 *4
print(result)
print(get_dict('Oh, it is python'))