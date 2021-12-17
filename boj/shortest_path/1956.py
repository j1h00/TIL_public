"""
    V개의 마을와 E개의 도로로 구성되어 있는 도시가 있다.
    도로는 마을과 마을 사이에 놓여 있으며, 일방 통행 도로이다. 
    마을에는 편의상 1번부터 V번까지 번호가 매겨져 있다고 하자.

    당신은 도로를 따라 운동을 하기 위한 경로를 찾으려고 한다. 
    운동을 한 후에는 다시 시작점으로 돌아오는 것이 좋기 때문에, 
    우리는 사이클을 찾기를 원한다. 단, 당신은 운동을 매우 귀찮아하므로, 
    사이클을 이루는 도로의 길이의 합이 최소가 되도록 찾으려고 한다.

    도로의 정보가 주어졌을 때, 
    도로의 길이의 합이 가장 작은 사이클을 찾는 프로그램을 작성하시오. 
    두 마을을 왕복하는 경우도 사이클에 포함됨에 주의한다.
"""
# 모든 사이클을 찾는 방법을 생각해보자 
# 두 정점 사이의 왕복도 사이클로 친다. 
# 1. 벨만포드를 통해 사이클 찾기 
# 2. bfs 를 통해 

# => 1, 2번 방법 모두 틀림 
# 플로이드 워셜을 통해 모든 정점에서 다른 정점으로의 최단 경로를 찾은 뒤 
# dp[i][i] => 자기 자신으로의 최단 경로를 찾으면 사이클의 최단 경로 이다. 
V, E = map(int, input().split())

INF = 10**9 
dp = [[INF]*(V) for _ in range(V)]

graph = {k:[] for k in range(V)}
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    dp[a-1][b-1] = c # dp 초기화 

# floyd-warshall 알고리즘
for k in range(V): # 중간 노드 
    for i in range(V):
        for j in range(V):
            # 원래 boj_11404 와 같은 플로이드 워셜에서는, a 와 b 가 같을 경우 0 으로 초기화, 
            # but 지금은 사이클을 찾아야 하므로, 굳이 필요하지 않다. 
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

answer = INF
for v in range(V):
    answer = min(answer, dp[v][v])

if answer == INF:
    print(-1)
else:
    print(answer)




