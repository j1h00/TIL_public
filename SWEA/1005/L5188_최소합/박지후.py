import sys
sys.stdin = open('input.txt')

# 미로 탐색과 같이 방향을 설정해주었습니다. 
directions = [(1, 0), (0, 1)] 

# stack 을 이용한 dfs 방식으로 처리하였고, 
# 경로의 합을 이용해 가지치기? 하였습니다. 
def search(start):
    visited = [[10**9]*N for _ in range(N)]
    visited[0][0] = arr[0][0] # 출발지는 0 으로 설정합니다. 

    stack = [start] 
    while stack:
        x, y = stack.pop()
        
        for dx, dy in directions: # 현재 위치에서 아래, 혹은 오른쪽 위치를 확인합니다. 
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] > visited[x][y] + arr[nx][ny]: # 새로운 경로의 합이 기존 경로의 합보다 크다면 가지 않도록 가지치기 
                visited[nx][ny] = visited[x][y] + arr[nx][ny] # 최소합으로 업데이트 하고
                stack.append((nx, ny)) # 다음 경로에 추가합니다. 

    return visited[N-1][N-1] 

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    
    start = (0, 0)
    answer = search(start)

    print(f'#{tc} {answer}')
    