import sys
from pprint import pprint
sys.stdin = open('input.txt')
from collections import deque

def bfs(start):
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if (0 <= nx < N and 0 <= ny < N) and (visited[nx][ny][1] < visited[x][y][1] + 1) and (arr[nx][ny] == arr[x][y] + 1):
                visited[nx][ny][0] = arr[start[0]][start[1]]
                visited[nx][ny][1] = visited[x][y][1] + 1
                queue.append((nx, ny))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    visited = [[[0, 1] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            start = (i,j)
            bfs(start)

    answer = 0
    answer_start = 0
    for row in visited:
        row.sort(key = lambda x: x[1])
        if row[-1][1] > answer:
            answer = row[-1][1]
            answer_start = row[-1][0]

    print(f'#{tc} {answer_start} {answer}')
    