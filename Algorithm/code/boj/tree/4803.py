"""
    그래프는 정점과 간선으로 이루어져 있다. 
    두 정점 사이에 경로가 있다면, 두 정점은 연결되어 있다고 한다. 
    연결 요소는 모든 정점이 서로 연결되어 있는 정점의 부분집합이다. 
    그래프는 하나 또는 그 이상의 연결 요소로 이루어져 있다.

    트리는 사이클이 없는 연결 요소이다. 트리에는 여러 성질이 있다. 
    예를 들어, 트리는 정점이 n개, 간선이 n-1개 있다. 
    또, 임의의 두 정점에 대해서 경로가 유일하다.

    그래프가 주어졌을 때, 트리의 개수를 세는 프로그램을 작성하시오.
"""
# pypy 로 시간초과 통과 
from collections import deque

def get_input():
    n, m = map(int, input().split())

    if n == 0:
        return {}, False

    graph = {k:[] for k in range(1, n+1)}

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    return graph, n

case = 0
while True: # input 이 (0, 0) 이 아닌 동안엔 계속 동작
    now_graph, N = get_input()

    if not N: # input 이 0, 0 인 경우 중단 
        break 

    case += 1 # 현재 케이스의 번호 

    visited = [0]*(N+1) # bfs 탐색을 하기 위한 방문 리스트 
    q = deque()

    cnt = 0 # 독립된 트리의 개수를 센다 
    for i in range(1, N+1): # 모든 정점을 시작점으로 하여 
        if not visited[i]: # 방문하지 않은 정점이라면
            visited[i] = 1 # 그 정점을 시작으로 같은 트리에 방문 표시를 한다. 
            q.append((i, 0))
        else: # 방문한 정점이면 넘어간다. 
            continue
        
        isTree = True 
        while q: # bfs 탐색 
            now, prev = q.popleft() # prev 는 트리 사이클 여부를 확인할 때, 예외처리 해준다. 

            for nxt in now_graph[now]:
                if visited[nxt] and nxt != prev: # 만약 이미 방문한 곳이면, 사이클을 형성한다. 이 때 nxt 가 prev 인 경우만 예외처리 해준다. 
                    isTree = False

                elif not visited[nxt]:
                    visited[nxt] = 1
                    q.append((nxt, now))

        if isTree:
            cnt += 1 # 트리의 개수를 1 추가 


    # 트리의 개수에 따른 출력 양식 
    if cnt > 1:
        print(f'Case {case}: A forest of {cnt} trees.')
    elif cnt == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: No trees.')

# 추가해야 할 사항 : 트리의 여부 
# 1. 트리에 사이클이 없는지, => 사이클 여부만 확인해도 통과 가능
# 2. 정점이 n, 간선이 n-1 인지
# 3. 두 정점 사이의 경로가 유일한지 