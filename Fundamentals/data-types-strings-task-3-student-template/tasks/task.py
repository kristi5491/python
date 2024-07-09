def replacer(s: str) -> str:
    replaced_words = []
    for word in s:
        if "'" in word:
            word = '"'
        elif '"' in word:
            word = "'"
        replaced_words.append(word)
    return ''.join(replaced_words)


print(replacer('mama\' has a \"banana\''))
