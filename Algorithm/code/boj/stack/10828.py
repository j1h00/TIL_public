import sys
class stack:
    def __init__(self):
        self.LIST = []
        self.SIZE = 0

    def push(self, num):
        self.LIST.append(num)
        self.SIZE += 1

    def pop(self):
        if self.SIZE == 0:
            print(-1)
            return
        TOP = self.LIST[-1]
        self.LIST = self.LIST[:-1]
        self.SIZE -= 1
        print(TOP)
    
    def size(self):
        print(self.SIZE)

    def empty(self):
        if self.SIZE == 0:
            print(1)
        else:
            print(0)
    
    def top(self):
        if self.SIZE == 0:
            print(-1)
            return
        print(self.LIST[-1])

def main():
    lines = int(sys.stdin.readline()[:-1])
    stack_0 = stack()
    for i in range(lines):
        INPUT_word = sys.stdin.readline()[:-1]
        if len(INPUT_word) > 5:
            stack_0.push(INPUT_word.split()[-1])
            continue
        elif INPUT_word == 'top':
            stack_0.top()
        elif INPUT_word == 'size':
            stack_0.size()
        elif INPUT_word == 'empty':
            stack_0.empty()
        elif INPUT_word == 'pop':
            stack_0.pop()

main()
