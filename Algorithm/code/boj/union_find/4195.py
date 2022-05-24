"""
어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 
두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

"""
def find(x):
    if x == p[x]:
        return x
    
    p[x] = find(p[x])
    return p[x]


# rank 를 사용하자 
def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        p[b] = a
        rank[a] += rank[b]

T = int(input())


for tc in range(T):
    F = int(input())

    p = {}
    rank = {}
    for _ in range(F):
        a, b = input().split()
        
        if a not in p:
            p[a] = a
            rank[a] = 1
        if b not in p:
            p[b] = b
            rank[b] = 1

        union(a, b)
        print(rank[find(a)])
        
    
    

    
        