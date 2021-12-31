"""
    신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 
    한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
    
    어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
    컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
    1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
"""
import sys
from collections import deque

N = int(sys.stdin.readline()[:-1])
M = int(sys.stdin.readline()[:-1])

graph = {k:[] for k in range(1, N+1)}

for i in range(M):
    k, v = map(int, sys.stdin.readline().split())
    graph[k].append(v)
    if k not in graph[v]:
        graph[v].append(k) # 양방향 그래프 

BFS = deque([1])
BFS_visited = [1]

while BFS:
    top = BFS.popleft()
    if graph[top]:
        for node in sorted(graph[top]):
            if node not in BFS_visited:
                BFS.append(node)
                BFS_visited.append(node)
                graph[top].remove(node) # 2021-12-03 remove 필요 없을듯..
            else:
                graph[top].remove(node)

print(len(BFS_visited)-1)