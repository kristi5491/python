class Cipher:

    def __init__(self, keyword: str):
        self.keyword = keyword
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        keyword_unique = ''.join(sorted(set(self.keyword), key=self.keyword.index))
        cipher_alphabet = keyword_unique + ''.join([char for char in alphabet if char not in keyword_unique])
        self.dict_d = {alphabet[i]: cipher_alphabet[i] for i in range(len(alphabet))}

    def encode(self, data: str):
        new_str = ''
        data_low = data.lower()
        for char in data_low:
            for key, val in self.dict_d.items():
                if key == char:
                    if char in data and data[data.index(char)].islower():
                        new_str += val
                        break
                    else:
                        new_str += val.upper()
                        break
                if char == ' ':
                    new_str += ' '
                    break
        return new_str


    def decode(self, data: str):
        new_str = ''
        data_low = data.lower()
        for char in data_low:
            for key, val in self.dict_d.items():
                if val == char:
                    if char in data and data[data.index(char)].islower():
                        new_str += key
                        break
                    else:
                        new_str += key.upper()
                        break
                if not char.isalpha():
                    new_str += char
                    break
        return new_str


cipher = Cipher("crypto")
print(cipher.encode("Hello world"))

print(cipher.decode("Fjedhc dn, atidsn"))