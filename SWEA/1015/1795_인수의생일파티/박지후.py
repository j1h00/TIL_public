import sys
sys.stdin = open('input.txt')
import heapq

def dijkstra(start):
    heap = [(0, start)]
    INF = 10**6
    distance = [INF]*(N+1)
    distance[start] = 0

    while heap:
        w, now = heapq.heappop(heap)

        if distance[now] < w:
            continue

        for dw, nxt in graph[now]:
            nw = w + dw 
            if distance[nxt] > nw:
                distance[nxt] = nw
                heapq.heappush(heap, (nw, nxt))

    return distance

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split()) # X == target house
    
    graph = {k:[] for k in range(1, N+1)}
    for _ in range(M):
        x, y, c= map(int, input().split())
        graph[x].append((c, y))
    
    X_to_i = dijkstra(X) # X 에서 나머지 정점으로의 최단 거리 
    i_to_X = [0]*(N+1) # i 에서 X 로의 최단 거리를 저장하는 배열
    answer = 0
    for i in range(1, N+1):
        i_to_X[i] = dijkstra(i)[X] # i 에서 나머지 정점으로의 최단거리를 구하여, X 로의 최단거리를 가져온다.
        total_i = X_to_i[i] + i_to_X[i] # X -> i -> X 최단 거리 계산
        answer = max(answer, total_i)

    print(f'#{tc} {answer}')