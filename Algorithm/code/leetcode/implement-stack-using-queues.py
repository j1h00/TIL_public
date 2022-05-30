# https://leetcode.com/problems/implement-stack-using-queues/

# implement LIFO stack using only two queues

from collections import deque


# 아래 풀이는 한 개의 큐만 사용
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x) # [prev, a, b, c] + new 
        for _ in range(len(self.q) - 1): # 마지막으로 append 한 요소만 남기고, 다시 꺼내서 집어넣는다. 
            self.q.append(self.q.popleft()) # [new, prev, a, b, c] 

    def pop(self) -> int: # stack 이므로, FIFO => 가장 최근에 넣은 new 를 꺼내야 한다.  
        return self.q.popleft() 

    def top(self) -> int:
        return self.q[0]
        
    def empty(self) -> bool:
        return len(self.q) == 0 