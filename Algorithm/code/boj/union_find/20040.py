"""
https://www.acmicpc.net/problem/20040
"""
import sys
input = sys.stdin.readline

def find(x):
    if x == p[x]:
        return x
    tmp = find(p[x])
    p[x] = tmp 
    return tmp 


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        if rank[a] > rank[b]:
            p[b] = a
            rank[a] += rank[b]
        else:
            p[a] = b
            rank[b] += rank[a]

n, m = map(int, input().split())

p = {}
rank = {}
flag = 0
for i in range(1, m+1):
    a, b = map(int, input().split())
    if flag:
        continue

    if a not in p:
        p[a] = a
        rank[a] = 1
    if b not in p:
        p[b] = b
        rank[b] = 1

    if find(a) == find(b):
        flag = i
    
    union(a, b)

print(flag)



