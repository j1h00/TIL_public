"""
    N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 
    당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 
    최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

    만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
    한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

    맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
"""
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = []

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline()[:-1])))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
visited = [[[0]*M for _ in range(N)] for i in range(2)] # 3차원 배열 visited 

queue.append((0, 0, 0))
visited[0][0][0] = 1 

done = False
answer = 0
while queue:
    h, x, y = queue.popleft() # h 는 3차원을 뜻하는데, 벽을 사용했는지 여부를 체크한다. 
    
    if x == N-1 and y == M-1: # 도착지에 도착 
        done = True
        answer = visited[h][x][y]
        break

    for i in range(4): 
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not arr[nx][ny] and not visited[h][nx][ny]: # 만약 벽이 아니고, 방문하지 않았다면  
                visited[h][nx][ny] = visited[h][x][y] + 1 # 그 위치까지 도달하는데 걸린 거리를 저장한다. 
                queue.append((h, nx, ny))

            elif arr[nx][ny] == 1 and not h: # 만약 벽이고, 벽을 부순 적이 없다면 (망치가 남아있다면)
                visited[1][nx][ny] = visited[0][x][y] + 1 # 차원을 옮겨서, 벽을 부쉈다고 가정하고 거리를 저장한다.
                queue.append((1, nx, ny))

if done:
    print(answer)
else:
    print(-1)