def union(*args) -> set:
    result = []
    for types in args:
        for char in types:
            result.append(char)
    return set(result)


def intersect(*args) -> set:
    final_set = set()
    intersect_set = {}
    size = 0
    for types in args:
        size += 1
        for char in types:
            intersect_set[char] = intersect_set.get(char, 0) + 1
    for key, val in intersect_set.items():
        if val == size: final_set.add(key)
    return final_set


print(union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']))
print(intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C')))