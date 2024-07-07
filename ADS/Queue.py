class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, elem):
        self.queue.append(elem)
    def dequeue(self):
        if len(self.queue)< 1:
            print('масив пустий')
        else:
            self.queue.pop(0)
    def display(self):
        for elem in self.queue:
            print(f'{elem}->', end='')

queue= Queue()
queue.enqueue(4)
queue.enqueue(3)
queue.enqueue(5)

queue.dequeue()
queue.display()

