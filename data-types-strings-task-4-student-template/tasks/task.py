def check_str(s: str):
    s = s.lower()
    no_space_text = ""
    for char in s:
        if char not in [' ', ',',  "'", '-']:
            no_space_text += char
    return no_space_text == no_space_text[::-1]


print(check_str("A man, a plan, a canal, Panama"))  # True
print(check_str("No 'x' in Nixon"))                 # True
print(check_str("що це"))                           # False
print(check_str("racecar"))                         # True
print(check_str("hello"))                          # False
