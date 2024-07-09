class Bird:
    def __init__(self, name: str):
        self.name = name
  
    def fly(self):
        return f'{self.name} bird can fly'

    def walk(self):
        return f"{self.name} bird can walk"


class FlyingBird(Bird):
    def __init__(self, name: str, ration: str = "grains"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return f'It eats mostly {self.ration}'

    def __str__(self):
        return f'{self.name} bird can walk and fly'


class NonFlyingBird:
    def __init__(self, name: str, ration: str = "fish"):
        self.name = name
        self.walk_result = Bird.walk(self)
        self.ration = ration

    def eat(self):
        return f"It eats mostly {self.ration}"

    def swim(self):
        return f'{self.name} bird can swim'

    def __str__(self):
        return f'{self.name} bird can eat and swim and walk'


class SuperBird(NonFlyingBird):
    def __init__(self, name, ration: str = "fish"):
        super().__init__(name,ration)
        self.walk_result = Bird.walk(self)
        self.fly_result = Bird.fly(self)
        self.swim_result = super().swim()
        self.eat_result = super().eat()

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"


b = Bird("Any")
print(b.walk())

p = NonFlyingBird("Penguin", "fish")
print(p.swim())
try:
   p.fly()
except AttributeError as e:
    print(e)
c = FlyingBird("Canary")
print(str(c))
print(c.eat())

s = SuperBird("Gull")
print(str(s))
