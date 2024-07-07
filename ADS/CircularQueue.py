class CircularQueue:
    def __init__(self, s):
        self.size = s
        self.queue = [None] * s
        self.front = self.rear = -1
    def __is_full(self):
        if((self.front ==0 and self.rear == self.size - 1) or self.front == self.rear + 1 ):
            return True
    def __is_empty(self):
         return  self.front == -1
    def enqueue(self, elem):
        if (self.__is_full()):
            print(f'Your queue is full')
        else:
            if (self.front == -1):
                self.front = 0
                self.rear = 0
                self.queue[self.front] = elem
                print(f'First element added: {elem}')
            else:
                self.rear =(self.rear + 1)% self.size
                self.queue[self.rear] = elem
                print(f'New element added: {elem}')
    def dequeue(self):
        if(self.__is_empty()):
            print(f'Your queue is empty')
        else:
            if (self.front == self.rear):
                self.front = self.rear = -1
            else: 
                element = self.queue[self.front]
                self.front = (self.front + 1) % self.size
                print(f'Element was deleted: {element}!')

    def display(self):
        if(self.__is_empty()):
            print(f'Your queue is empty')
        elif(self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                print(f'{self.queue[i]}->', end='')
            print()
        else:
            for i in range(self.front, self.size):
                print(f'{self.queue[i]}->', end='')
            for i in range(0, self.rear + 1):
                print(f'{self.queue[i]}->', end='')
            print()     
queue = CircularQueue(4)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)


queue.enqueue(1)

queue.dequeue()
queue.display()

queue.enqueue(12)
queue.dequeue()
queue.enqueue(7)
queue.dequeue()

queue.display()
