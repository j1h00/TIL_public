import sys
sys.stdin = open('input.txt')
from collections import deque

# 최소 연산이 몇번인지 구해야한다. => bfs?
# bfs 로 가능한 모든 연산을 탐색. 목표 수를 찾으면 바로 중단하고 return 최솟값.
def bfs(start, end):
    queue = deque([(start, 0)])
    visited = [0] * (10**6 + 1)
    visited[start] = 1
    while queue:
        now, cnt = queue.popleft()

        if now == end:
            return cnt 

        nxts = [now+1, now-1, now*2, now-10]
        for nxt in nxts:
            if 0 < nxt <= 10**6 and not visited[nxt]:
                queue.append((nxt, cnt+1))
                visited[nxt] = 1
        

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    print(f'#{tc} {bfs(N, M)}')