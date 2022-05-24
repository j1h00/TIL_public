# 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있다. 
# 그리고 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있다. 
# 마을의 이장은 위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다

# 그래프를 둘로 분리하고, MST 를 만족하면 된다. 

# 첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다. 
# N은 2이상 100,000이하인 정수이고, M은 1이상 1,000,000이하인 정수이다.
import heapq


N, M = map(int, input().split())

graph = { k:[] for k in range(1, N+1) }
for i in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

# 일단 마을을 둔로 분리하자 
# 어떤 기준으로 분리할 것인가! 
# 먼저 마을을 나누지 말고, 최소 신장 트리로 만든 다음에 
# 그 중에서 가장 긴 경로를 잘라서 나누자


# 다익스트라 !== 프림 알고리즘 .. 
INF = 10 ** 9
distance = [INF] * (N + 1)
heap = [(0, 1)]
distance[1] = 0

while heap:
    w, now = heapq.heappop(heap)

    if w > distance[now]:
        continue

    for nw, nxt in graph[now]:
        if distance[nxt] > distance[now] + nw:
            distance[nxt] = distance[now] + nw
            heapq.heappush(heap, (distance[nxt], nxt))

print(distance)






