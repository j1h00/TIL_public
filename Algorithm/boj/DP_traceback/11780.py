"""
    n(1 ≤ n ≤ 100)개의 도시가 있다. 
    그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 
    각 버스는 한 번 사용할 때 필요한 비용이 있다.

    모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.
"""
# 플로이드 2
from pprint import pprint

N = int(input())
M = int(input())

INF = 10**9
dp = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    if dp[a][b] > c:
        dp[a][b] = c

# floyd-warshall algorithm
# 경로를 어디에 저장할 것인가 
# dp 배열 or 다른 배열 
path = [[[] for _ in range(N+1)] for _ in range(N+1)] # 경로를 저장할 배열 
for k in range(1, N+1): # 중간 경로 
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                dp[i][j] = 0
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                path[i][j] = path[i][k] + [k] + path[k][j] # 경로를 path 배열에 저장해준다. 
                # 경로는 i ~ k 까지의 경호 + k + k ~ j 까지의 경로를 모두 포함해야 한다. 
                
for i in range(1, N+1):
    for j in range(1, N+1):
        if dp[i][j] == INF: # relaxation 되지 않은 INF 값들은 0 으로 바꾸어준다. 
            dp[i][j] = 0
    print(*dp[i][1:])

for i in range(1, N+1):
    for j in range(1, N+1):
        if dp[i][j]:
            print(len(path[i][j]) + 2, i, *path[i][j], j) # 시작과 끝을 포함하여 출력 
        else:
            print(0)

