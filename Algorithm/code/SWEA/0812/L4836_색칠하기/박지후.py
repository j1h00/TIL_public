import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    purple = 0

    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if arr[r][c]*color == 2:
                    arr[r][c] = 3
                    purple += 1
                else:
                    arr[r][c] = color

    print(f'#{tc} {purple}')