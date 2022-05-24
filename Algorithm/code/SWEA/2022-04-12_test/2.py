import sys
sys.stdin = open('input2.txt', 'r')


def check_vertical(i, j):
    global MIN_H
    result = []
    # 위 쪽으로 체크
    tmp = i + 1
    while True:
        if tmp >= N:
            break

        if tmp - i > MIN_H:
            return [], False

        if arr[tmp][j] == 3:
            return (tmp, j), True

        if arr[tmp][j]:
            result.append((tmp, j, abs(tmp - i)))
            break
        tmp += 1

    # 아래 쪽으로 체크
    tmp = i - 1
    while True:
        if tmp < 0:
            break

        if tmp - i > MIN_H:
            return [], False

        if arr[tmp][j] == 3:
            return (tmp, j), True

        if arr[tmp][j]:
            result.append((tmp, j, abs(tmp - i)))
            break
        tmp -= 1
    return result, False


def dfs(now, jump, path):
    global MIN_H
    if jump > MIN_H:
        return

    x, y = now
    if arr[x][y] == 3:
        MIN_H = min(MIN_H, jump)
        return

    possible, flag = check_vertical(x, y)
    if flag:
        nx, ny = possible
        jump = max(jump, abs(nx - x))
        MIN_H = min(MIN_H, jump)
        return

    for dx, dy in side_position:
        possible.append((x + dx, y + dy, 0))

    for nx, ny, now_jump in possible:
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny]:
            visited[nx][ny] = 1
            dfs((nx, ny), max(jump, now_jump), path + [(nx, ny)])
            visited[nx][ny] = 0

    return


side_position = [(0, 1), (0, -1)]
T = int(input())
for tc in range(1, T+1):
    MIN_H = 100
    N, M = map(int, input().split())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    S = ()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                S = (i, j)
                break
    visited = [[0] * M for _ in range(N)]
    visited[S[0]][S[1]] = 1
    dfs(S, 0, [S])

    print("#%d %d" % (tc, MIN_H))


