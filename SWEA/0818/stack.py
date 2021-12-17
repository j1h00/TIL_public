class Stack:
    def __init__(self, *args):
        self.data = list(args)

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        value = self.data[-1]
        self.data = self.data[:-1]
        return value

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not bool(self.data)

    def __str__(self):
        return f'{self.data} <- top'


s = Stack(1, 2, 3)
s.push(4)
print(s)
print(s.is_empty())
print(s.top())
v1 = s.pop()
v2 = s.pop()

