class Field:
    __value = None

    def __init__(self):
        self.__value = None

    def set_value(self, val):
        self.__value = val
        return self.__value

    def get_value(self):
        return self.__value


fild = Field()


print(fild.set_value(5))

print(fild.get_value())