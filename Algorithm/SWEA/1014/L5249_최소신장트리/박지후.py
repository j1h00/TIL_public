import sys
sys.stdin = open('input.txt')
import heapq

# MST 를 찾을 때 사용하는 prim 알고리즘
def prim(start):
    visited[start] = 1 # 시작점을 방문 표시 
    heap = graph[start] # 시작점에서 인접한 그래프를 heap 에 추가 
    heapq.heapify(heap)
    total_w = 0 # 간선의 가중치의 총합 

    while heap: 
        w, now = heapq.heappop(heap) # heappop 으로 가중치 w 의 최소값 보장 !!!

        if not visited[now]: # 아직 방문하지 않은 곳인 경우 
            visited[now] = 1 # 방문 표시 
            total_w += w # 간선 총합에 더해줌. 

            for nw, nxt in graph[now]: # 현재 정점에서 인접한 모든 정점에 대해 
                if not visited[nxt]: # 방문하지 않았다면 
                    heapq.heappush(heap, (nw, nxt)) # heap 에 추가 

    return total_w

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    
    graph = {k:[] for k in range(V+1)}
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1].append((w, n2))
        graph[n2].append((w, n1)) # 양방향 그래프 

    visited = [0] * (V+1)
    start = 0 
    print(f'#{tc} {prim(start)}')