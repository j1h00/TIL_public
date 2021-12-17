"""
    n(1≤n≤1,000)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스가 있다. 
    우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 
    그러면 A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라. 
    항상 시작점에서 도착점으로의 경로가 존재한다.
"""
# 최소비용 구하기 2
# 최소비용 + 경로 
# 다익스트라 이용.
# 기존에 사용하던 다익스트라는 최소 비용만 저장했었다. 
# 경로를 어디에 저장할 것인가
# => prev 에 저장하여 역으로 traceback!

import heapq

N = int(input())
M = int(input())

graph = {k:[] for k in range(1, N+1)}
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))

S, E = map(int, input().split())

def dijkstra(S, E):
    INF = 10**9
    dp = [INF]*(N+1)
    prev = [0]*(N+1)

    q = [(0, S)]
    heapq.heapify(q)
    dp[S] = 0
    while q:
        w, now = heapq.heappop(q)

        if w > dp[now]:
            continue

        for nxt_w, nxt in graph[now]:
            if dp[nxt] > dp[now] + nxt_w:
                dp[nxt] = dp[now] + nxt_w
                prev[nxt] = now
                heapq.heappush(q, (nxt_w, nxt))
    
    now = E
    answer = [E]
    while now != S:
        now = prev[now]
        answer.append(now)

    print(dp[E])
    print(len(answer))
    print(*answer[::-1])

dijkstra(S, E)

                
                
    
    

