# 인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.


from pprint import pprint

from collections import deque
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, L, R = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

def bfs(i, j, populations, visited):
    q = deque([(i, j)])
    visited[i][j] = 1
    total = populations[i][j]
    union = [(i, j)]

    while q:
        r, c = q.popleft()

        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and L <= abs(populations[nr][nc] - populations[r][c]) <= R:
                q.append((nr, nc))
                visited[nr][nc] = 1
                union.append((nr, nc))
                total += populations[nr][nc]

    avg = total // len(union)
    for r, c in union:
        populations[r][c] = avg

    return len(union)

day = 0
while True:
    visited = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                count = bfs(i, j, arr, visited)
                if count > 1:
                    flag = True
    if flag:
        day += 1
    else:
        break
print(day)
        

        




