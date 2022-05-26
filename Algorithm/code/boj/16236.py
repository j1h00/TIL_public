# 아기 상어 https://www.acmicpc.net/problem/16236


from collections import deque


directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# find locations                
fish_count = 0
shark = ()
for i in range(N):
    for j in range(N):
        now = arr[i][j] 
        if now:
            if now == 9:
                shark = (i, j)
            else:
                fish_count += 1

eat_count = 0
size = 2

def find_fish(shark, size):
    print("@@", shark, size)
    visited = [[0] * N for _ in range(N)]
    x, y = shark 
    visited[x][y] = 1

    answer = []
    flag = False  
    min_dis = 41 # max_N * 2 + 1
    q = deque([(x, y, 0)])
    while q:
        x, y, dis = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy 
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and dis <= min_dis:
                if 0 < arr[nx][ny] <= size:
                    answer.append((nx, ny, dis + 1))
                    min_dis = dis + 1
                    continue

                if not arr[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny, dis + 1))
                    continue
    if answer:
        print(sorted(answer, key= lambda x: (x[2], x[0], x[1])))
        return sorted(answer, key= lambda x: (x[2], x[0], x[1]))[0]
    else:
        return []

time = 0
while fish_count:
    print("---------------------------")
    selected_fish = find_fish(shark, size)
    print(selected_fish)
    print(time, size, eat_count)
    if not selected_fish:
        break 
    else:
        x, y = shark
        nx, ny, dis= selected_fish
        time += dis 
        fish_count -= 1
        if arr[nx][ny] == size:
            eat_count += 1

        arr[nx][ny] = 0
        arr[x][y] = 0
        shark = (nx, ny)

    if size == eat_count:
        size += 1
        eat_count = 0
    
print(time)
    

    

