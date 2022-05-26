import sys
sys.stdin = open('input.txt')



def dfs(now, stack, cnt):

    if cnt == 7:
        result.append(stack)
        return

    x, y = now[0], now[1]
    for dx, dy in d:
        nx = x + dx
        ny = y + dy 
        if 0 <= nx < N and 0 <= ny < N:
            dfs((nx, ny), stack + str(arr[nx][ny]), cnt + 1)
    

T = int(input())
for tc in range(1, T+1):
    N = 4
    arr = []
    for i in range(4):
        arr.append(list(map(int, input().split())))

    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = []
    for i in range(N):
        for j in range(N):
            start = (i,j)
            dfs(start, str(arr[i][j]), 1)

    answer = len(set(result))

    print(f'#{tc} {answer}')