"""
    체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 
    나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
"""
import sys
from collections import deque

T = int(sys.stdin.readline()[:-1])

for tc in range(T):
    I = int(sys.stdin.readline()[:-1])
    x, y = map(int, sys.stdin.readline().split())
    N, M = map(int, sys.stdin.readline().split())

    arr = [[0]*I for _ in range(I)]

    d = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)] # 나이트의 이동 경로 

    queue = deque()
    queue.append((x, y))

    done = False
    while queue:
        x, y = queue.popleft()

        if x == N and y == M:
            done = True
            break

        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < I and 0 <= ny < I:
                if not arr[nx][ny]:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx, ny))
                    
    print(arr[N][M])
