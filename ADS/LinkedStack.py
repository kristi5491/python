class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,elem):
        new_node = Node(elem)
        if (self.head == None):
            self.head = new_node
            print(f'First element added: {elem}')
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            print(f'element added: {elem}')
    def delete_from_the_front(self):
        temp = self.head
        self.head = self.head.next
        del temp
        print(f'Element from the begining deleted')
    def delete_from_end(self):
        end = self.head
        prev = None
        while(end.next):
            prev= end
            end = end.next
        prev.next = None
        print('element from the end deleted')
    def display(self):
        current= self.head
        while current:
            print(f'{current.elem}->' ,end='')
            current = current.next
        print()
         
    
elem = LinkedList()
elem.insert(1)
elem.insert(2)
elem.insert(3)
elem.insert(4)

elem.display()

elem.delete_from_the_front()
elem.display()
elem.delete_from_end()
elem.display()