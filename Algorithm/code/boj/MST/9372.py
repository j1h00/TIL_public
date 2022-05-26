"""
상근이의 여행
https://www.acmicpc.net/problem/9372
"""

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    graph = {k:[] for k in range(1, N+1)}
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # 최소 신장 트리인가? 
    # 비행기 항로에 거리가 주어지지 않고 
    # 단순히 "가장 적은 종류" 의 비행기 항로를 이용하며 된다. 
    # 이미 방문한 국가를 방문해도 상관 없음 

    # 이상한 문제가 분명하다. 
    print(N-1)



