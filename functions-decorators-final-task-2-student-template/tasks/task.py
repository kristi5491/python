from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    array = []
    new_word = ""
    curr_index = 0
    old_index = 0
    if len(indexes) == 1:
        return [s]
    for index in indexes:
        curr_index = index - old_index
        old_index = index
        for letter in s:
            if s.index(letter) == index - 1 and index - 0 > 0:
                s = s[index:]
                new_word += letter
                array.append(new_word)
                new_word = ''
                if len(array) + 1 == len(indexes) + 1:
                    return array
                break
            elif s.index(letter) == curr_index - 1:
                s = s[curr_index:]
                new_word += letter
                array.append(new_word)
                new_word = ''
                if len(array) + 1 == len(indexes) + 1:
                    array.append(s)
                    return array
                break
            else:
                new_word += letter

    return array


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_by_index("no luck", [42]))