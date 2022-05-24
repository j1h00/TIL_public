import sys
sys.stdin = open('input.txt')

T = int(input())


def count(N):
    global cnt
    cnt += 1
    for i in tree[N]:
        count(i)


for tc in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = list([] for _ in range(E+2))

    for i in range(E):
        tree[lst[2*i]].append(lst[2*i+1])

    cnt = 0
    count(N)
    print(f'#{tc} {cnt}')