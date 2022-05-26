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
        graph[e].append(s)
        
    S, G = map(int, input().split())

    # 그래프 경로 문제와 동일하게 bfs 로 경로를 찾습니다. 
    queue = deque([S])
    visited = [-1]*(V+1)
    visited[S] = 0 # visited 는 시작 위치로 부터의 거리를 저장합니다. 
    found = 0
    while queue:
        now = queue.popleft()
        if now == G:
            found = 1
            break

        for nxt in graph[now]:
            if visited[nxt] < 0 :
                queue.append(nxt)
                visited[nxt] = visited[now] + 1 # 다음 정점은 현재 정점보다 (시작 위치로부터) 1 만큼 더 멉니다. 

    if not found:
        visited[G] = 0 
    print(f'#{tc} {visited[G]}') # 도착 지점의 visited 값이 답입니다. 
