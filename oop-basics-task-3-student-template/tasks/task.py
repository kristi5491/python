class Counter:
    def __init__(self, start=None, stop=None):
        self.start = start
        self.stop = stop
        self.current = start if start is not None else 0

    def get(self):
        return self.current

    def increment(self):
        if self.start is None and self.stop is None:
            self.current += 1
            return self.current
        elif self.stop is None:
            if self.current >= self.start + 100:
                return self.current
            self.current += 1
            return self.current
        elif self.start is None:
            if self.current >= self.start + 100:
                return self.current
            self.current += 1
            return self.current
        else:
            if self.current >= self.stop:
                return 'Maximal value is reached.'  # or raise an error, or reset, depending on desired behavior
            self.current += 1
            return self.current


c = Counter(start=42)
c.increment()
print(c.get())

c = Counter()
c.increment()
print(c.get())

c.increment()
print(c.get())

c = Counter(start=42, stop=43)
c.increment()
print(c.get())

print(c.increment())
print(c.get())