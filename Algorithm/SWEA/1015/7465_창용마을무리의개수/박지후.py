import sys
sys.stdin = open('input.txt')


def find_set(x):
    if x == p[x]:
        return p[x]
    else:
        return find_set(p[x])

def union(x, y):
    if find_set(x) != find_set(y): # 같은 무리가 아니라면, 
        p[find_set(x)] = find_set(y) # 대표 번호로 업데이트 


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = list(range(N+1))
    
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)

    cnt = 0
    for x in range(1, N+1):
        if x == p[x]:
            cnt += 1

    print(f'#{tc} {cnt}')