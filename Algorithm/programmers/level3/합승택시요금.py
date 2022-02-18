import heapq

# 다익스트라로 구하자~ 
# => floyd warshall 이 더 효율적일 수도 있겠다. 
# 3 <= n <= 200
def dijkstra(n, start, graph):
    INF = 10**9
    dp = [INF]*(n+1)
    dp[start] = 0

    q = [(0, start)]
    heapq.heapify(q)

    while q:
        w, now = heapq.heappop(q)

        if w > dp[now]:
            continue
        
        for nw, nxt in graph[now]:
            if dp[nxt] > dp[now] + nw:
                dp[nxt] = dp[now] + nw
                heapq.heappush(q, (w + nw, nxt))
    return dp

def solution(n, s, a, b, fares): # n 지점갯수, s 출발지점, a 도착, b 도착, 택시요금 
    graph = {k:[] for k in range(1, n+1)}
    for x, y, w in fares:
        graph[x].append((w, y))
        graph[y].append((w, x))

    dp_s = dijkstra(n, s, graph)

    answer = dp_s[a] + dp_s[b]
    for i in range(1, n+1):
        dp_i = dijkstra(n, i, graph)
        answer = min(answer, dp_s[i] + dp_i[a] + dp_i[b]) # 
        
    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))