"""
    동혁이는 친구들과 함께 여행을 가려고 한다. 
    한국에는 도시가 N개 있고 임의의 두 도시 사이에 길이 있을 수도, 없을 수도 있다. 
    동혁이의 여행 일정이 주어졌을 때, 이 여행 경로가 가능한 것인지 알아보자. 
    물론 중간에 다른 도시를 경유해서 여행을 할 수도 있다. 
    예를 들어 도시가 5개 있고, A-B, B-C, A-D, B-D, E-A의 길이 있고, 
    동혁이의 여행 계획이 E C B C D 라면 E-A-B-C-B-C-B-D라는 여행경로를 통해 목적을 달성할 수 있다.

    도시들의 개수와 도시들 간의 연결 여부가 주어져 있고, 
    동혁이의 여행 계획에 속한 도시들이 순서대로 주어졌을 때 가능한지 여부를 판별하는 프로그램을 작성하시오. 
    같은 도시를 여러 번 방문하는 것도 가능하다.
"""

def find(x):
    if x == p[x]:
        return x
    return find(p[x])

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        p[a] = b
    else:
        p[b] = a


N = int(input())
M = int(input())

p = [i for i in range(N+1)]

arr = []
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for j in range(1, N+1):
        if tmp[j-1]: # 만약 1이라면, 
            union(i, j)

plan = list(map(int, input().split()))

answer = 'YES'
first = find(plan[0])
for i in range(1, M):
    if first != find(plan[i]):
        answer = 'NO'
        break

print(answer)