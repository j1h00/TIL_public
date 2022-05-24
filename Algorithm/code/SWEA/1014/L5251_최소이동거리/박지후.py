import sys
sys.stdin = open('input.txt')
import heapq


def dijkstra(N):
    distance = [float('inf')]*(N+1)
    heap = [(0, 0)]
    distance[0] = 1

    while heap:
        w, now = heapq.heappop(heap)

        if distance[now] < w:
            continue

        for dw, nxt in graph[now]:
            nw = w + dw
            if distance[nxt] > nw:
                distance[nxt] = nw 
                heapq.heappush(heap, (nw, nxt))
    
    return distance[N]


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())

    graph = {k:[] for k in range(N+1)}
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    print(f'#{tc} {dijkstra(N)}')