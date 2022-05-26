from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

arr = []

N = len(arr)
queue = deque()
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            queue.append((i,j))

while queue:
    x, y= queue.popleft()

    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N and not arr[nx][ny]:
            queue.append((nx, ny))
            arr[nx][ny] = arr[x][y] + 1
            last = arr[nx][ny]

print(last)