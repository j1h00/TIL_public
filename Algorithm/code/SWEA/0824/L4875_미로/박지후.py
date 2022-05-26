import sys
sys.stdin = open('input.txt')

def dfs(stack):
    global flag 

    if flag:    # 이미 3을 만난 상태면 돌아갑니다.
        return 

    x, y = stack.pop()
    for dx, dy in d:
        nx = x + dx
        ny = y + dy 
        if 0 <= nx <= N-1 and 0 <= ny <= N-1 and not visited[nx][ny]:
            if miro[nx][ny] == 3: # 도착하면 멈추고, flag 를 통해 쭉 빠져나갑니다.
                flag = 1
                return 
            elif not miro[nx][ny]: # 0 을 만나면
                visited[nx][ny] = 1 # 이동하여 방문했음을 표시하고
                dfs(stack + [(nx, ny)]) # 이동한 지점부터 다시 시작합니다.
            
        else:   # 범위를 벗어나거나, 이미 방문한 경우.
            continue
    

T = int(input())
d = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 네방향을 모두 탐색합니다.
for tc in range(1, T+1):
    N = int(input())
    miro = []

    for i in range(N):
        miro.append(list(map(int, input())))

    stack = []
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                stack.append((i,j)) # 완전탐색으로 2를 찾습니다.

    visited = [[0]*N for _ in range(N)]
    flag = 0
    dfs(stack[:])
    
    print(f'#{tc} {flag}')
    
    