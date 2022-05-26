import sys
from pprint import pprint
sys.stdin = open('input.txt')


def dfs(stack, cnt):
    global max_cnt
    d = ((1,0), (0,1), (-1,0), (0,-1))
    if cnt > max_cnt: # 가장 긴 경로를 max_cnt 에 저장한다. 
        max_cnt = cnt

    used, x, y = stack.pop() # used 는 공사를 했는지 안했는지 뜻한다. 
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if 0<= nx <= N-1 and 0 <= ny <= N-1 and not visited[nx][ny]: # 범위 내에 있고, 방문하지 않은 길이라면
            if arr[nx][ny] < arr[x][y]: # 만약 내려갈 수 있는 길이라면 
                visited[nx][ny] = 1 # 방문하고 그 곳에서부터 다시 dfs 한다. 
                dfs(stack + [(used, nx, ny)], cnt + 1)
                visited[nx][ny] = 0 # dfs 가 끝나고 나면, 방문 기록을 지운다. 
            elif not used and arr[nx][ny] - K < arr[x][y]: # 만약 공사를 한 적이 없고, 공사를 해서 갈 수 있는 길이라면
                temp = arr[nx][ny] # 원래 높이를 잊지 않도록 저장해둡니다.
                arr[nx][ny] = arr[x][y] - 1 # 공사해서 내려갈 수 있는 최대 높이로 만들고 
                visited[nx][ny] = 1 # 방문하여, 그 곳에서부터 다시 dfs 한다. 
                dfs(stack + [(1, nx, ny)], cnt + 1)
                arr[nx][ny] = temp # dfs 가 끝나고 나면, 공사했던 높이를 초기화하고
                visited[nx][ny] = 0 # 방문 기록도 지운다. 


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    highest = 0
    for row in arr:
        highest = max(highest, max(row)) # 최고 높이를 구한다. 
    
    tops = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == highest:
                tops.append((i,j)) # 최고 높이의 위치를 모두 찾는다. 

    max_cnt = 0
    for start in tops: # 최고 높이를 시작으로 
        visited = [[0]*N for _ in range(N)]
        i, j = start
        visited[i][j] = 1 
        dfs([(0, i, j)], 1) # 내려가는 경로를 찾는다. 
        
    print(f'#{tc} {max_cnt}')
    