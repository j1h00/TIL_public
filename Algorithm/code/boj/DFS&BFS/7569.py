"""
    7576 의 3차원 버전 
    정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 
    이러한 N개의 줄이 H번 반복하여 주어진다.
"""

import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

queue = deque()
tomato = []
zero = 0
for k in range(H): # k 는 쌓아올린 상자의 z 축 위치를 뜻한다. 
    tomato.append([])
    for i in range(N):
        tomato[k].append(list(map(int, sys.stdin.readline().split())))
        for j in range(M):
            if tomato[k][i][j] == 1: # 마찬가지로 익은 토마토 위치를 찾는다. 
                queue.append((k,i,j))
            elif tomato[k][i][j] == 0:
                zero += 1

dx = [-1, 1, 0, 0, 0, 0] 
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

cnt = 0
while queue:
    z, x, y = queue.popleft()
    for i in range(6): # 3차원 이동 
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
            if tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = tomato[z][x][y] + 1
                zero -= 1
                cnt = tomato[nz][nx][ny] -1
                queue.append((nz,nx,ny))
if zero:
    print(-1)
else:
    print(cnt)
