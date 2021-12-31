import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    max_height = 255
    b_height = list(map(int, input().split()))
    b_array = [[0]*max_height for _ in range(-2, N+2)]

    for i in range(N):
        for j in range(b_height[i]):
            b_array[i][j] = 1

    count = 0
    for i in range(N):
        for j in range(b_height[i]):
            if b_array[i][j]:
                if b_array[i-2][j] + b_array[i-1][j] + b_array[i+1][j] + b_array[i+2][j] == 0:
                    count += 1

    print(f'#{tc} {count}')