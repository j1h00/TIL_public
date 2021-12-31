"""
    방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 
    단, 모든 간선의 가중치는 10 이하의 자연수이다.
"""
# 다익스트라 
import sys
import heapq
# 다익스트라 알고리즘에서 우선순위 큐를 사용하는 이유는 갱신 횟수의 감소를 위해..?

INF = 10**9 
V, E = map(int, sys.stdin.readline().split())
K = int(input())
graph = {k:[] for k in range(1, V+1)}

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w,v))

heap = [(0, K)]
visited = [INF]*(V+1)
while heap:
    w, now = heapq.heappop(heap) # 현재 정점에 연결된 정점들 가운데, 간선의 가중치가 가장 낮은 것을 뽑는다. 
    
    if w > visited[now]: # => heapq 를 사용하다 보니, 동일한 노드라도 큐에 저장이 될 수 있어서 처리해준다.  
        continue

    while graph[now]: # 그 정점에 연결된 정점들을 찾는다. 
        nxt = graph[now].pop() # 
        if nxt[0] + w < visited[nxt[1]]: # 만약 가중치를 더한 값이, 현재 그 곳까지의 최단 경로 길이보다 작다면
            visited[nxt[1]] = nxt[0] + w # 최단 경로를 업데이트 한다. 
            heapq.heappush(heap, (visited[nxt[1]], nxt[1]))

for i in range(1, V+1):
    if i == K:
        print(0)
    elif visited[i] == INF:
        print('INF')
    else:
        print(visited[i])
    
