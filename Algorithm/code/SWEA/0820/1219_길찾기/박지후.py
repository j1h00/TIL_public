import sys
from collections import deque

sys.stdin = open('input.txt')

T = 10

# bfs version
for tc in range(T):
    tc, n = map(int, input().split())
    v1 = [0]*100
    v2 = [0]*100
    e = list(map(int, input().split()))
    for i in range(n):
        k, v = e[2*i:2*i+2]
        if not v1[k]:
            v1[k] = v
        else:
            v2[k] = v

    queue = deque()
    queue.append(0)
    done = 0
    while queue:
        now = queue.popleft()
        if v1[now] == 99 or v2[now] == 99:
            done = 1
            break
        for nxt in [v1[now], v2[now]]:
            if nxt:
                queue.append(nxt)
        v1[now] = 0
        v2[now] = 0

    print(f'#{tc} {done}')

