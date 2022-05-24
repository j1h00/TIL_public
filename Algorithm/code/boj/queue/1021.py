import sys
from collections import deque

N, M = [int(_) for _ in sys.stdin.readline()[:-1].split(" ")]
num_list = [int(_) for _ in sys.stdin.readline()[:-1].split(" ")]

cnt = 0 
queue = deque(range(1, N+1))
size = N
for i in num_list:
    left = 0
    while True:
        now = queue[0]
        if now == i:
            queue.popleft()
            size -= 1
            break
        else:
            queue.append(queue.popleft())
            left += 1
    right = size - left + 1
    if left > right:
        cnt += right 
    else:
        cnt += left
print(cnt)
    