"""
    트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다.
    트리의 지름을 구하는 프로그램을 작성하시오.
"""
# 다익스트라로 모든 정점 사이의 거리를 찾아서 구하려고 했으나 시간초과 실패!
# 1167_2.py 에선 BFS 를 사용해보자 
import heapq
INF = 10**9

def dijkstra(start, N):
    global INF
    
    distance = [INF]*(N+1)
    distance[0] = 0
    distance[start] = 0

    q = [(start, 0)] 
    heapq.heapify(q)

    while q:
        now, now_d = heapq.heappop(q)

        if distance[now] < now_d:
            pass
        for nxt, nxt_d in graph[now]:
            if distance[nxt] > distance[now] + nxt_d:
                distance[nxt] = distance[now] + nxt_d
                heapq.heappush(q, (nxt, distance[nxt]))

    return distance

N = int(input())

graph = {v:[] for v in range(1, N+1)}

for i in range(1, N+1):
    info = list(map(int, input().split()))
    for j in range((len(info)-2)//2):
        graph[i].append((info[2*j+1], info[2*j+2]))

answer = 0
for s in range(1, N+1):
    answer = max(answer, max(dijkstra(s, N)))

print(answer)


