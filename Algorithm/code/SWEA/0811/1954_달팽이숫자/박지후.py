# 달팽이
import sys

sys.stdin = open("input.txt")

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


T = int(input())

for tc in range(T):
    N = int(input())
    A = [[0]*N for i in range(N)]

    cnt = 1
    x, y = 0, 1
    k = 0
    while cnt <= N*N:
        nx = x + di[k] 
        ny = y + dj[k]
        if 0 <= nx < N and 0 <= ny < N:
            if A[nx][ny] == 0:
                A[nx][ny] = cnt
                cnt += 1
                i, j = nx, ny
        else:
            k = (k+1)%4

    print(f'#{tc}\n{A}')