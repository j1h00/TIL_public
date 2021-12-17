import sys
sys.stdin = open('input2.txt')

def dfs(now, memo):
    global answer 

    if memo[1] > answer[1]:
        answer = memo

    x, y = now[0], now[1]
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if (0 <= nx < N and 0 <= ny < N) and (arr[nx][ny] == arr[x][y] + 1):
            visited[nx][ny] = 1
            dfs((nx, ny), (memo[0], memo[1] + 1))
            visited[nx][ny] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    answer = (0, 0)

    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            start = (i,j)
            visited[i][j] = 1
            dfs(start, (arr[i][j], 0))
            visited[i][j] = 0

    print(f'#{tc} {answer[0]} {answer[1] + 1}')
    