import sys
from pprint import pprint
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1)) # 상 우 하 좌 
    pipes = {
        1:(0, 1, 2, 3),
        2:(0, 2), # 상 하 
        3:(3, 1), # 좌 우 
        4:(0, 1), # 상 우
        5:(2, 1), # 하 우 
        6:(2, 3), # 하 좌 
        7:(0, 3), # 상 좌
    }
    N, M, R, C, L = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    
    visited = [[0]*M for _ in range(N)]
    queue = deque([(R, C)])
    visited[R][C] = 1
    cnt = 1 # 갈 수 있는 위치의 수를 저장 
    while queue: # bfs
        x, y = queue.popleft()
        for d in pipes[arr[x][y]]: # 현재 파이프 종류에 따라, 갈 수 있는 방향 d 를 차례대로 점검한다.  
            dx, dy = directions[d]
            nx = x + dx
            ny = y + dy 
            if (0 <= nx < N and 0 <= ny < M) and visited[x][y] < L and not visited[nx][ny] and arr[nx][ny]: # (1) 범위 내에서, (2) 소요된 시간 내에서 (3) 방문한 적이 없고 (4) 파이프가 존재해야한다. 
                if (d+2)%4 in pipes[arr[nx][ny]]: # 다음에 갈 곳에 있는 파이프의 방향이, 현재 파이프의 방향과 대응 가능하다면. 
                    queue.append((nx,ny)) # queue 에 추가 
                    visited[nx][ny] = visited[x][y] + 1 # 방문 표시 및, 소요 시간 저장
                    cnt += 1 # 방문한 위치의 수를 증가

    print(f'#{tc} {cnt}')

