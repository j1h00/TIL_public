"""
    (취익)B100 요원, 요란한 옷차림을 한 서커스 예술가 한 쌍이 한 도시의 거리들을 이동하고 있다. 
    너의 임무는 그들이 어디로 가고 있는지 알아내는 것이다. 
    우리가 알아낸 것은 그들이 s지점에서 출발했다는 것, 그리고 목적지 후보들 중 하나가 그들의 목적지라는 것이다. 그
    들이 급한 상황이기 때문에 목적지까지 우회하지 않고 최단거리로 갈 것이라 확신한다. 이상이다. (취익)

    어휴! (요란한 옷차림을 했을지도 모를) 듀오가 어디에도 보이지 않는다. 
    다행히도 당신은 후각이 개만큼 뛰어나다. 
    이 후각으로 그들이 g와 h 교차로 사이에 있는 도로를 지나갔다는 것을 알아냈다.

    이 듀오는 대체 어디로 가고 있는 것일까?
"""
import heapq

# 최단 경로를 저장한다. 
def dijkstra(start):
    heap = [start]
    visited = [float('inf')]*(n+1)
    visited[start[1]] = 0 # 출발점을 초기화 한다. 
    while heap:
        w, now = heapq.heappop(heap)
        for nw, nxt in graph[now]:
            if visited[nxt] > nw + w:
                visited[nxt] = nw + w
                heapq.heappush(heap, (visited[nxt], nxt))
    return visited

T = int(input())
for tc in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = {k:[] for k in range(1, n+1)}

    for i in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))

    candidates = []
    for i in range(t):
        candidates.append(int(input()))

    # 방법 1
    # 시작점 s 로부터 다익스트라 => 후보지로의 최소 경로를 찾는다.
    # 경로에 g => h 길이 포함되는지 확인한다.  
    # 반례 : 최단 경로가 여러 개인 경우.. 위 함수는 하나의 경로만 저장하므로 찾기 어렵다.. ㅠ
    
    # 방법 2 
    # s => g => h => 후보지 
    # s => h => g => 후보지 
    # 두 가지 경우를 찾고, 최단거리와 일치하는지 확인한다. => good! 
    path_s = dijkstra((0,s))
    path_g = dijkstra((0,g))
    path_h = dijkstra((0,h))
    
    answer = []
    for c in candidates:
        A1 = path_s[g] + path_g[h] + path_h[c]
        A2 = path_s[h] + path_h[g] + path_g[c]
        if A1 == path_s[c] or A2 == path_s[c]:
            answer.append(c)

    answer.sort()
    print(*answer)
    