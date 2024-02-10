class Stack:
    def __init__(self):
        self.__stack = []

    def add_to_stack(self, num):
        self.__stack.append(num)
        print(f'ваше число добавлине до стеку{self.__stack}')

    def delate_from_stack(self,num_searched):
        if num_searched in self.__stack:
            self.__stack.remove(num_searched)
            print(f'ваще число видалено з списку. ocь оновлений лист {self.__stack}')
        else:
            print('такої цифри нема в стеку')
    def delate_last_num(self):
        self.__stack.pop()
        print(f'ваще число видалено з списку. ocь оновлений лист {self.__stack}')

    def check_is_empty(self):
        if not self.__stack:
            print(f'ваш стек пустий []')
        else:
            print('ваш список НЕ пустий')

stack = Stack()
stack.add_to_stack(5)
stack.add_to_stack(4)
stack.add_to_stack(3)

stack.delate_last_num()
stack.delate_last_num()
stack.delate_last_num()

stack.check_is_empty()

