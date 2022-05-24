import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(start):
    queue = deque([start])

    while queue:
        now = queue.popleft()

        for nxt in graph[now]: # 인접한 사람을 모두 확인 
            if not visited[nxt]: # 방문하지 않은 경우 
                queue.append(nxt) # queue 에 추가 
                visited[nxt] = 1 
                # 방문표시 
                # 1. 한 사람이 같은 조에서 중복되게 탐색되지 않도록함. 
                # 2. 이미 어떤 조에 포함된 한 사람이 다른 조에 포함되지 않도록함. 


# 서로소집합 문제인가 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    request = list(map(int, input().split()))

    graph = {k:[] for k in range(1, N+1)} # dictionary 에 저장 
    for i in range(M):
        graph[request[2*i]].append(request[2*i + 1]) # 지목을 할수도, 당할수도 있으므로 양방향 그래프
        graph[request[2*i + 1]].append(request[2*i])

    visited = [0] * (N+1)
    cnt = 0
    for n in range(1, N+1): # 모든 사람을 한번씩 확인.  
        if not visited[n]: # 만약 어떤 조에 포함되지 않은 사람일 경우 
            bfs(n) # 그 사람을 시작으로 bfs 탐색 후 
            cnt += 1 # 조의 수 + 1 

    print(f'#{tc} {cnt}')