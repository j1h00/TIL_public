"""
    루트 없는 트리가 주어진다. 
    이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
"""
from collections import deque

N = int(input())

graph = {k:[] for k in range(1, N+1)}
visited = [0]*(N+1)
parent = [0]*(N+1)
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque() 
queue.append(1)
visited[1] = 1 
while queue:
    now = queue.popleft()
    for nxt in graph[now]:
        if not visited[nxt]:
            parent[nxt] = now
            visited[nxt] = 1 
            queue.append(nxt)

for i in range(2, N+1):
    print(parent[i])
    

