from collections import deque

N, M = map(int, input().split())
miro = []
for i in range(N):
    miro.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
queue.append((0,0))

while queue:
    x, y = queue.popleft()
    if x == N-1 and y == M-1:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and miro[nx][ny]:
            miro[nx][ny] = miro[x][y] + 1
            queue.append((nx,ny))
    miro[x][y] = 0 
    
print(miro[N-1][M-1])
