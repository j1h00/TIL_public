import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly = []
    for i in range(N):
        fly.append(list(map(int, input().split())))

    max_kill = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for row in range(i, i+M):
                total += sum(fly[row][j:j+M])
            max_kill = max(max_kill, total)

    print(f'#{tc} {max_kill}')
