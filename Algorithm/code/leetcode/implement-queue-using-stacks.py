# https://leetcode.com/problems/implement-queue-using-stacks/

# failed
class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        newStack = []
        for _ in range(len(self.stack) - 1):
            newStack.append(self.stack.pop())
        self.stack = newStack 

    def pop(self) -> int:
        self.stack.pop()

    def peek(self) -> int:
        if not self.empty():
            self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []