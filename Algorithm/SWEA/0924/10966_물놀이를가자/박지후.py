import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs(start, N, M):
    d = ((1,0), (-1,0), (0,1), (0,-1)) 
    queue = deque([start])
    while queue: 
        x, y = queue.popleft()
        for dx, dy in d: # 4 방향을 모두 탐색 
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M: # 범위 내에서 
                if visited[nx][ny] > visited[x][y] + 1: 
                    visited[nx][ny] = visited[x][y] + 1 # 더 작은 수로 업데이트 
                    queue.append((nx,ny)) # queue 에 추가 
                    # 만약 더 이상 작은 수로 업데이트 할 수 있는 경우가 없다면, while loop 을 빠져나오게 된다. 
                if arr[nx][ny] == 'W': # 만약 그 곳이 물이었다면
                    visited[nx][ny] = 0 # 0 으로 표시한다. 
    
                
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(input())

    visited = [[10**3 * 2]*M for _ in range(N)] # N, M 의 최대 길이 10**3 만큼 저장.
    flag = False # 2중 for loop 빠져나오기 위한 flag
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W': # W 의 위치를 하나 찾는다. 
                visited[i][j] = 0 # 방문하였음을 0 으로 표시한다. 
                bfs((i,j), N, M) # i,j 에서 bfs 시작
                flag = True # bfs 종료 후 루프를 빠져 나온다. 
                break 
        if flag:
            break

    answer = 0
    for row in visited: # visited 배열에 적힌 최소 이동 횟수를 모두 합해준다. 
        answer += sum(row) 

    print(f'#{tc} {answer}')
    