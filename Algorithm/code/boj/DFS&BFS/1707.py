"""
    그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 
    그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

    그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.
"""
import sys
from collections import deque

T = int(sys.stdin.readline()[:-1])

def bfs():
    visited = [0]*(v+1) # 1차원 배열로 방문 표시 (1, -1 로 구분)
    bipartite = True

    for start in range(1, v+1): # 1 ~ v 사이에서, 한 점을 잡아 시작 
        if not visited[start]: # 아직 방문한 적이 없는 점이라면 
            visited[start] = 1 # 방문 표시를 하고 
            queue = deque()
            queue.append(start)

            while queue: # bfs 탐색 
                x = queue.popleft()
                for y in graph[x]:
                    if not visited[y]: # 방문한 적이 없다면 
                        visited[y] = -1 * visited[x] # 인접한 곳이므로, 다른 그래프로 표시함. 
                        queue.append(y)
                    else:
                        if visited[y] == visited[x]: # 만약 서로 인접한 곳이, 같은 그래프로 표시되어있다면 
                            bipartite = False # 이분 그래프로 나눌 수 없다. 
                            queue = []
                            break 

        if not bipartite: # for 문 빠져나옴.
            return bipartite

    return bipartite

for tc in range(T):
    v, e = map(int, sys.stdin.readline().split())
    graph = {k: [] for k in range(1, v+1)}
    for i in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a) # 양방향 그래프 저장 

    is_bipartite = bfs()

    if is_bipartite:
        print('YES')
    else:
        print('NO')

                    

