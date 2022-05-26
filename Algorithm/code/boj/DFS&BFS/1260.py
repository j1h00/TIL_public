import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph1 = {k:[] for k in range(1, N+1)}
graph2 = {k:[] for k in range(1, N+1)}

for i in range(M):
    k, v = map(int, sys.stdin.readline().split())
    graph1[k].append(v)
    if k not in graph1[v]:
        graph1[v].append(k)
    graph2[k].append(v)
    if k not in graph2[v]:
        graph2[v].append(k)

DFS = [V]
DFS_visited = [V]

BFS = deque([V])
BFS_visited = [V]

while DFS:
    top = DFS[-1]
    if graph1[top]:
        if min(graph1[top]) not in DFS_visited:
            DFS.append(min(graph1[top]))
            graph1[top].remove(min(graph1[top]))
            DFS_visited.append(DFS[-1])
        else:
            graph1[top].remove(min(graph1[top]))
    else:
        DFS.pop()
print(" ".join([str(_) for _ in DFS_visited]))

while BFS:
    top = BFS.popleft()
    if graph2[top]:
        for node in sorted(graph2[top]):
            if node not in BFS_visited:
                BFS.append(node)
                BFS_visited.append(node)
                graph2[top].remove(node)
            else:
                graph2[top].remove(node)

print(" ".join([str(_) for _ in BFS_visited]))

# def get_map(K):
#     field = {i:[] for i in range(1, K+1)}
#     for k, v in map(int, sys.stdin.readline()[:-1]):
#         if v not in field[k]:
#             field[k].append(v)
#             field[v].append(k)
#     return field