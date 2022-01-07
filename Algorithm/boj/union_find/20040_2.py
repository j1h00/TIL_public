"""
https://www.acmicpc.net/problem/20040
"""
import sys
input = sys.stdin.readline

def find(x):
    while p[x] != x:
        x = p[x]
    return x


def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        p[b] = a
    else:
        p[a] = b

n, m = map(int, input().split())

p = [i for i in range(n)]
for i in range(1, m+1):
    a, b = map(int, input().split())

    if find(a) == find(b):
        print(i)
        sys.exit(0)
    
    union(a, b)

print(0)



