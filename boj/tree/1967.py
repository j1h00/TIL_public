"""
    트리(tree)는 사이클이 없는 무방향 그래프이다. 
    트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 
    트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 
    이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.
    트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.

    입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 
    트리의 지름을 구해서 출력하는 프로그램을 작성하시오.
"""
# 트리의 지름 => 그래프 탐색 2번으로 가능하다. 
from collections import deque

def bfs(start, N): # bfs 
    q = deque() # deque 이용 
    q.append(start)
    visited = [0]*(N+1) # 방문 표시 
    visited[start] = 1

    while q:
        now = q.popleft()

        for nxt, nxt_w in graph[now]:
            if not visited[nxt]:
                visited[nxt] = visited[now] + nxt_w
                q.append(nxt)

    most_far = (0, 0) # 가장 멀리 있는 정점을 찾는다. 
    for max_id, far in enumerate(visited):
        if far > most_far[1]:
            most_far = (max_id, far)

    return most_far

N = int(input())

graph = {k:[] for k in range(1, N+1)}

for i in range(N-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))

any_far = bfs(1, N)
most_far = bfs(any_far[0], N)

# bfs 탐색 시, visited 에 방문 기록 및 정점으로 부터의 거리를 저장하는데, 
# 처음 시작 정점을 visited 1 로 표시해야 하기 때문에, 마지막에 1을 빼준다. 
print(most_far[1]-1) 

