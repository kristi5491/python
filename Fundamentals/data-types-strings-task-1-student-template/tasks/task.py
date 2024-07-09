def get_fractions(a_b: str, c_b: str) -> str:
    x1 = a_b.split('/')
    x2 = c_b.split('/')
    return f"{a_b} + {c_b} = {int(x1[0]) + int(x2[0])}/{x1[1]}"


print(get_fractions("5/4", "3/4"))
