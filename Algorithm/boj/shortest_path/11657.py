"""
    N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 버스가 M개 있다. 
    각 버스는 A, B, C로 나타낼 수 있는데, A는 시작도시, B는 도착도시, C는 버스를 타고 이동하는데 걸리는 시간이다. 
    시간 C가 양수가 아닌 경우가 있다. 
    C = 0인 경우는 순간 이동을 하는 경우, C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우이다.

    1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.

    만약 1번 도시에서 출발해 어떤 도시로 가는 과정에서 시간을 무한히 오래 전으로 되돌릴 수 있다면 첫째 줄에 -1을 출력한다. 
    그렇지 않다면 N-1개 줄에 걸쳐 각 줄에 1번 도시에서 출발해 2번 도시, 3번 도시, ..., N번 도시로 가는 가장 빠른 시간을 순서대로 출력한다. 
    만약 해당 도시로 가는 경로가 없다면 대신 -1을 출력한다.
"""
import sys
input = sys.stdin.readline

# 경로 가중치에 음수값이 있는 경우. => 싸이클 생성 될 수 있음을 조심 => 벨만 포드 
def bellman_ford(N, graph):
    start = 1
    distance = [0, 0] + [float('inf')]*(N-1)
    for i in range(N): # N 번 수행한다. 
        for node in graph: # 모든 정점에 대하여 
            for nxt in graph[node]: 
                # relaxation 
                if distance[nxt[0]] > distance[node] + nxt[1]:
                    distance[nxt[0]] = distance[node] + nxt[1]
                    if i == N-1: # N 번 실행했는데, relaxation 이 가능한 경우, cycle 생성을 의미한다. 
                        print(-1) # 이 경우, N 번 실행했을 때 relaxation 이 가능하다는 것은 무한히 relaxation 이 가능하다 (무한히 값이 작아질 수 있다) 는 것을 의미 
                        return
    return distance


N, M = map(int, input().split())

graph = {k:[] for k in range(1, N+1)}
for i in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

distance = bellman_ford(N, graph)
if distance: # cycle 이 없는 경우 
    for i in range(2, N+1): # 어떤 도시로 갈 수 있는 경로가 없다면 
        if distance[i] == float('inf'):
            print(-1)
            continue
        print(distance[i])