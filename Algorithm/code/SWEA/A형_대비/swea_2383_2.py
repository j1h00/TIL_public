from collections import deque
            
T = int(input())
for tc in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    stairs = {}
    people = deque()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                people.append((i,j))
            elif arr[i][j] > 1:
                stairs[(i,j)] = [] 
    
    while people:
        x, y = people.popleft()

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    people.append((nx,ny))
                for stair in stairs.keys:
                    if (nx,ny) == stair and (nx,ny) not in stairs[(nx,ny)]:
                        stairs[(nx,ny)].append(((nx, ny), arr[x][y] + 1))
    
    print(stair)

                
        