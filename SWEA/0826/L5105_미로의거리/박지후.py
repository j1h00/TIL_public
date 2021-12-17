import sys
from collections import deque
sys.stdin = open('input.txt')

# bfs 함수는 시작 위치를 받아서, bfs 방식으로 길을 찾습니다. 3에 도착하면 시작 위치로부터의 거리를 리턴합니다. 
def bfs(queue):
    visited = [[0]*N for _ in range(N)] # visited 는 시작 위치로부터의 거리를 저장합니다. 
    while queue:
        x, y = queue.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy 
            if 0 <= nx <= N-1 and 0 <= ny <= N-1 and not visited[nx][ny]:
                if miro[nx][ny] == 3: # 도착하면
                    return visited[x][y]
                elif not miro[nx][ny]: # 0 을 만나면
                    visited[nx][ny] = visited[x][y] + 1 # 다음 위치는 현재 위치보다, 시작점으로부터 1 더 멉니다. 
                    queue.append((nx,ny))
    return 0 

T = int(input())
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for tc in range(1, T+1):
    N = int(input())
    miro = []

    for i in range(N):
        miro.append(list(map(int, input())))

    queue = deque()
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                queue.append((i,j)) # 완전탐색으로 2를 찾습니다.

    cnt = bfs(queue)
    
    print(f'#{tc} {cnt}')
    
    