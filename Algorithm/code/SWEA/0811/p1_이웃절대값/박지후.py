import sys

sys.stdin = open("input.txt")

T = int(input())


for tc in range(T):
    arr = []
    N = int(input())
    for i in range(N):
        arr.append(list(map(int, input().split())))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result = 0

    for x in range(N):
        for y in range(N):
            for _ in range(4):
                nx = x + dx[_]
                ny = y + dy[_]
                if 0 <= nx < N and 0 <= ny < N:
                    result += abs(arr[x][y] - arr[nx][ny])
    print(f'#{tc} {result}')