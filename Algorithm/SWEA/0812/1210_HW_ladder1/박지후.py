import sys

sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    tc = int(input())
    ladder = []
    for i in range(100):
        ladder.append([0, *map(int, input().split()), 0])

    y = 99
    x = 0
    for j in range(1, 101):
        if ladder[y][j] == 2:
            x = j
            break

    while y > 0:
        if ladder[y][x-1]:
            x = x-1
        elif ladder[y][x+1]:
            x = x+1
        else:
            y -= 1
        ladder[y][x] = 0

    print(f'#{tc} {x-1}')