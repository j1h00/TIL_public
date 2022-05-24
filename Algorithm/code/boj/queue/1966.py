import sys
from collections import deque

test_case = int(sys.stdin.readline()[:-1])

for i in range(test_case):
    N, M = [int(_) for _ in sys.stdin.readline()[:-1].split(" ")]
    queue = deque([int(_) for _ in sys.stdin.readline()[:-1].split(" ")])
    priority = sorted(queue, reverse = True)
    top_priority = 0
    size = N
    now = M
    while True:
        if queue[0] == priority[top_priority]:
            if now == 0:
                print(N-size+1)
                break
            queue.popleft()
            top_priority += 1
            now -= 1
            size -= 1
        else:
            queue.append(queue.popleft())
            now -= 1
        if now < 0:
            now = size-1
