"""
    n(2 ≤ n ≤ 100)개의 도시가 있다. 
    그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 
    각 버스는 한 번 사용할 때 필요한 비용이 있다.

    모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.
"""
import sys
import heapq
input = sys.stdin.readline

# 다익스트라로 풀이 불가!!
def dijkstra(start, n, graph):
    heap = [(0, start)]
    distance = [float('inf')]*(n+1)
    distance[start] = 0 # 출발점을 초기화 한다. 
    while heap:
        w, now = heapq.heappop(heap)
        for nw, nxt in graph[now]:
            if distance[nxt] > nw + w:
                distance[nxt] = nw + w
                heapq.heappush(heap, (distance[nxt], nxt))

    for i in range(1, n+1):
        if distance == float('inf'):
            distance[i] = 0
    return distance


n = int(input())
m = int(input())


graph = {k:[] for k in range(1, n+1)}
for i in range(m):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))

for i in range(1, n+1):
    start = i
    distance = dijkstra(start, n, graph)
    print(*distance[1:])
