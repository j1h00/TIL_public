"""
    방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 
    또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 
    그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

    세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 
    하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 
    1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.
"""
import sys
import heapq

def dijkstra(start):
    heap = [start]
    visited = [INF]*(N+1)
    visited[start[1]] = 0 # 출발점을 초기화 한다. 

    while heap: # heap 이 비어있지 않은 동안엔 
        w, now = heapq.heappop(heap)
        
        if w > visited[now]:
            continue

        for nw, nxt in graph[now]:
            if visited[nxt] > nw + w:
                visited[nxt] = nw + w
                heapq.heappush(heap, (visited[nxt], nxt))
    return visited

INF = float('inf')
N, E = map(int, sys.stdin.readline().split())

graph = {k:[] for k in range(1, N+1)}

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

v1, v2 = map(int, sys.stdin.readline().split()) # 거쳐야 하는 두 정점이 주어진다.  

from_start = dijkstra((0,1)) # 1 에서 다른 정점들 까지의 최단 경로 
from_v1 = dijkstra((0,v1)) # v1 에서 다른 정점들 까지의 최단 경로 
from_v2 = dijkstra((0,v2)) # v2 에서 다른 정점들 까지의 최단 경로 

A1 = from_start[v1] + from_v1[v2] + from_v2[N] # 1 => v1 => v2 => N 
A2 = from_start[v2] + from_v2[v1] + from_v1[N] # 1 => v2 => v1 => N
A = min(A1, A2) # 둘 중 짧은 경로를 택한다. 
print( A if A < INF else -1)

