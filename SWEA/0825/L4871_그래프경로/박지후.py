import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = {k:[] for k in range(1, V+1)}
    for i in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
    
    S, G = map(int, input().split())

    found = 0
    queue = deque([S])
    visited = [0]*(V+1)
    visited[S] = 1
    while queue:
        now = queue.popleft()
        if now == G:
            found = 1
            break

        for nxt in graph[now]:
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = 1
    
    print(f'#{tc} {found}')
