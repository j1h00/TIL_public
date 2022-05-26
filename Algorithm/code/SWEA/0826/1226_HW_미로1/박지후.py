import sys
from collections import deque
sys.stdin = open('input.txt')

def find_start(miro, N):
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                return (i,j)

directions = ((-1,0), (1,0), (0,-1), (0,1))

T = 10
for tc in range(1, T+1):
    tc = int(input())
    miro = []
    N = 16
    for i in range(N):
        miro.append(list(map(int, input())))

    start = find_start(miro, N)
    queue = deque([start])

    # bfs 방식으로 탐색했습니다. 
    found = 0
    while queue:
        x, y = queue.popleft()
        for d in directions:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                if miro[nx][ny] == 3: # 3을 만나면 
                    found = 1
                    queue = []
                    break 
                elif not miro[nx][ny]: # 0 을 만나면
                    miro[nx][ny] = 1
                    queue.append((nx, ny))
                    
    print(f'#{tc} {found}')