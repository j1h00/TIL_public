# 비용 편익(Cost-Benefit) = (U1 + U2 + U3 + U4)2

import sys
sys.stdin = open('input1.txt', 'r')


def cal(cells):
    result = 0
    for i, j in cells:
        result += arr[i][j]
    return result ** 2


def dfs(cells, now, count):
    global MAX_U

    if count == 4:
        now_u = cal(cells)
        if MAX_U < now_u:
            MAX_U = now_u
        return

    x, y = now
    directions = d_odd if now[1] % 2 else d_even
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(cells + [(nx, ny)], (nx, ny), count + 1)
            visited[nx][ny] = 0

    return


def check_exception(x, y):
    global MAX_U

    result = 0
    for directions in d_tri:
        temp_result = arr[x][y]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                temp_result += arr[nx][ny]
            else:
                break
        result = max(result, temp_result ** 2)

    MAX_U = max(result, MAX_U)


T = int(input())

d_tri_up = [(-1, 0), (1, 1), (1, -1)]
d_tri_down = [(1, 0), (0, 1), (0, -1)]
d_tri = [d_tri_up, d_tri_down]

d_odd = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1)]
d_even = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1)]

for tc in range(1, T+1):
    MAX_U = 0
    M, N = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            visited[i][j] = 1
            dfs([(i, j)], (i, j), 1, )
            visited[i][j] = 0

            check_exception(i, j)

    print("#%d %d" % (tc, MAX_U))

