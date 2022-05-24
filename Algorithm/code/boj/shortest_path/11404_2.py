# 플로이드 와셜 
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())


graph = [[float('inf')]*n for _ in range(n)]
for i in range(m):
    A, B, C = map(int, input().split())
    if graph[A-1][B-1] > C:
        graph[A-1][B-1] = C 
    
# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.
# Floyd-Warshall algorithm 
# 삼중 for loop 을 거치므로, 그래프의 크기가 작아 세제곱 시간을 적용해도 문제 없을 때 사용 가능.
for r in range(n): # 중간 노드가 될 번호를 가장 바깥의 for 문에 위치시킨다. 
    for a in range(n):
        for b in range(n):
            if a == b: # 같은 도시일 경우, 최단 경로 길이 0 
                graph[a][b] = 0
            graph[a][b] = min(graph[a][b], graph[a][r] + graph[r][b]) 
            # (a => b) vs (a => r => b) 
            # a 에서 b 로 직접 가는 경로는 없을 수 있지만, r 을 통해서 가능할 수도 있다. 

for i in range(n):
    for j in range(n):
        if graph[i][j] == float('inf'):
            graph[i][j] = 0 
        print(graph[i][j], end = " ")
    print()