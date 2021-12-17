import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    pascal = [[1] * _ for _ in range(1, N + 1)]

    for i in range(2, N):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    print(f'#{tc}')
    for row in range(N):
        print(*pascal[row])

