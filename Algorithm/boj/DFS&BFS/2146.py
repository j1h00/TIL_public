from collections import deque

# plan 1 : 시간 초과 : 모든 위치마다 bfs 를 두번씩 실행해야함.. 
# 1. 시작 위치를 잡는다.
# 2. bfs 로 시작 위치와 같은 구역에 있는 위치들만 visited 에 1로 표시 ('현재 구역' 표시)

# 3. 현재 구역을 제외한 나머지 부분은 bfs 로 탐색하면서, 거리로 채운다. 
    # 3-1. arr[x][y] == 0 (바다) 인 구역을 탐색하여 거리는 distance 에 저장, visited 에 1로 표시 
    # 3-2. arr[x][y] == 1 (육지) 인 구역을 만나면 
        # 3-2-1. visited 가 1 이면 '현재 구역'과 같은 구역이므로 pass
        # 3-2-2. visited 가 0 이면 '현재 구역'과 다른 구역이므로, 지금까지 온 거리를 return 

# plan 2 
# 1. 먼저, 모든 구역을 bfs 를 이용하여 각기 다른 숫자로 grouping 혹은 numbering 한다. 
# 2. 각각 numbering 된 구역에 대하여, 다른 구역으로의 최소 거리를 확인한다. 
    # 2-1. 현재 구역의 모든 위치를 시작점으로 하여 모두 queue 에 넣고, bfs 돌면서 다른 구역을 만났을 때 그 거리를 return 
    #

def plan1_bfs(start):
    queue = deque([start])

    # 2
    visited = [[0]*N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    distance = [[0]*N for _ in range(N)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))

    queue = deque([start])
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N: # 범위 내에 있는 경우 
                if not arr[nx][ny] and not visited[nx][ny]: # 바다이고, 가보지 않은 경우 
                    distance[nx][ny] = distance[x][y] + 1 # 길이를 1 추가한 다리를 놓는다. 
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                elif arr[nx][ny] and not visited[nx][ny]: # 육지이고, 가보지 않은 경우 
                    return distance[x][y] # 다른 육지로의 최단 경로!!
    return False

def plan2_grouping(i, j, group_num):
    queue = deque([(i,j)])
    arr[i][j] = group_num
    group_visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] and not group_visited[nx][ny]:
                arr[nx][ny] = group_num
                group_visited[nx][ny] = 1
                queue.append((nx, ny))

def plan2_find(group_num):
    distance = [[10**6]*N for _ in range(N)]
    
    queue = deque()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == num:
                queue.append((i, j))
                distance[i][j] = 0 # bfs 탐색 시 현재 구역으로 돌아오는 것을 막는다. 

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and distance[nx][ny] > distance[x][y] + 1: # 최소 거리가 가능한 길만 간다.
                if arr[nx][ny]: # 다른 구역인 경우 
                    return distance[x][y] # 현재 다리의 길이를 return 
                else: # 바다인 경우 
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

                    
N = int(input())

arr = [] 
for i in range(N):
    arr.append(list(map(int, input().split())))

directions = [(1,0), (0,1), (-1,0), (0,-1)]

# grouping
group_visited = [[0]*N for _ in range(N)] # 같은 구역을 두번 체크하지 않도록. 
group_num = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] and not group_visited[i][j]: # i,j 와 같은 구역을 모두 group_num 으로 표시. 
            plan2_grouping(i, j, group_num)
            group_num += 1

# find
min_len = 10**6
for num in range(1, group_num):
    flag = False
    for i in range(N):
        for j in range(N):
            if arr[i][j] == num:
                min_len = min(min_len, plan2_find(num))
                flag = True
                break 
        if flag:
            break 
print(min_len)