"""
    창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 
    보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
    하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 
    대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
    철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

    정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
"""
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
tomato = []
zero = 0
for i in range(N):
    tomato.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M):
        if tomato[i][j] == 1: # 익은 토마토의 위치 
            queue.append((i,j))
        elif tomato[i][j] == 0:
            zero += 1 # 익지 않은 토마토의 개수 

cnt = 0
while queue: 
    x, y = queue.popleft() # bfs 로 익은 토마토에서부터 시작 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if tomato[nx][ny] == 0: # 익지 않은 토마토를 만나면 
                tomato[nx][ny] = tomato[x][y] + 1 # 그 토마토가 익을 때 까지 걸린 날짜로 바꾼다.  
                zero -= 1 # 익지 않은 토마토의 개수를 하나 뺀다. 
                cnt = tomato[nx][ny] -1 # cnt 는 그 토마토가 익을 때 까지 걸린 날짜!
                queue.append((nx,ny))
if zero:
    print(-1)
else:
    print(cnt)
