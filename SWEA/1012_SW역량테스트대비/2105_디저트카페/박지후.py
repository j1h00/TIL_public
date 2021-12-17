import sys
sys.stdin = open('input.txt')

# 사각형의 가장 위쪽 꼭지점에서 시계방향으로 dfs 탐색하는 함수 정의 
def dfs(start, now, cnt, prev_d): # dfs 탐색 
    global MAX_cnt 

    x, y = now[0], now[1]
    
    if x == start[0]+1 and y == start[1]-1 and cnt > MAX_cnt: # 위쪽 꼭지점 바로 앞에까지 도달한 경우 
        MAX_cnt = cnt 
        return 

    # 무조건 시계방향으로만 탐색하도록 방향 설정. 
    for d in [prev_d, prev_d+1]: # (현재 방향)과 (현재 방향에서 90도 꺽은 바로 다음 방향) 모두 탐색 
        dx, dy = directions[d]
        nx = x + dx 
        ny = y + dy 
        if 0 <= nx < N and 0 <= ny < N and not check_dessert[arr[nx][ny]]: # 아직 먹지 않은 디저트인 경우 
            check_dessert[arr[nx][ny]] = 1
            dfs(start, (nx, ny), cnt+1, d)
            check_dessert[arr[nx][ny]] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    directions = [(1, 1), (1, -1), (-1, -1), (-1, 1), (0, 0)] # 오른쪽 아래, 왼쪽 아래, 왼쪽 위, 오른쪽 위 // 시계방향
    # [ ..., (0, 0)]
    # 1. 처음 시작 시 방향을 directions[-1] 로 설정하여, 무조건 오른쪽 아래로만 이동하게함.
    # 2. 시계방향으로 돌아서 마지막 꼭지점을 지나 오른쪽 위로 이동할 때 인덱스 에러 방지 

    MAX_cnt = 1
    check_dessert = [0] * 101 # 디저트 번호 1 ~ 100 까지.. 먹은 디저트는 1로 표시. 
    for i in range(N-2): # 아래로 한바퀴 돌아야 하므로, padding 2 필요 
        for j in range(1, N-1): # 마찬가지로 최소 한바퀴 돌려면, 왼쪽 오른쪽 padding 1 필요 
            start = (i, j)
            check_dessert[arr[i][j]] = 1
            dfs(start, start, 1, -1) 
            check_dessert[arr[i][j]] = 0

    if MAX_cnt == 1: # 찾지 못한 경우 
        MAX_cnt = -1

    print(f'#{tc} {MAX_cnt}')