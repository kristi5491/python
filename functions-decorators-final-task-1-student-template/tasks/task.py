from typing import List


def split(data: str, sep=None, maxsplit=-1):
    new_data = []
    if sep is None:
        if maxsplit == 0:
            return [data.strip()]
        current_word = ''
        for char in data:
            if char != ' ':
                current_word += char
            else:
                if current_word:
                    new_data.append(current_word)
                    current_word = ''
        if current_word:
            new_data.append(current_word)
    else:
        parts = data.split(sep, maxsplit)
        new_data.extend(parts)
        if maxsplit >= 0 and len(parts) < maxsplit + 1:
            new_data.extend([''] * (maxsplit - len(parts) + 1))

    return new_data



if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']