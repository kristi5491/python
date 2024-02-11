class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def push_elem(self,element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            print('перший елемент добавлено')
        else:
            while (self.head.next != None):
                new_node = self.head
            print('елемент добавлено в список')


    def pop_element(self):
        previous = None
        while(self.head.next is not None):
            previous = self.head
            self.haed = self.head.next
        if previous == None:
            self.head = None
        else:
            previous.next = None

        return self.head.value
            

print('елемент видалено')



listt = LinkedList()
listt.push_elem(2)
listt.push_elem(3)
listt.push_elem(4)

listt.pop_element()
                
