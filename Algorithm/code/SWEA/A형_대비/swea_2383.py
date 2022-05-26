from collections import deque


def bfs(person):
    visited = [[0]*N for _ in range(N)]
    q = deque()
    q.append(person)

    cnt = 0 
    while q:
        x, y, id, d = q.popleft()

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = 1
                if arr[nx][ny] > 1: # 계단에 도착함.
                    distance[(nx,ny)].append((person[2], d+1))
                    cnt += 1
                    if cnt == 2: # 계단 두개에 모두 도착하면 
                        return 
                else:
                    q.append((nx, ny, id, d+1))
    
            
T = int(input())
for tc in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    people = deque()
    person_cnt = 0

    distance = {}
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
               people.append((i, j, person_cnt, 0))
               person_cnt += 1
            elif arr[i][j] > 1:
                distance[(i,j)] = []

    for person in people:
        bfs(person)

    # {(1, 4): [(0, 4), (1, 3), (2, 2), (3, 4), (4, 2), (5, 7)], 
    #  (4, 2): [(0, 5), (1, 4), (2, 3), (3, 3), (4, 3), (5, 2)]}
    stair_q = []
    for d_list in distance.values():
        stair_q.append(sorted(d_list, key = lambda x: x[1]))

    time = 1
    flag = 0
    while flag < 2:

    




# 1. bfs 로 계단까지의 거리 구하기
# 2. 어떤 사람이 어떤 계단을 이용해야 하는지 어떻게 구별할까 
    # 2-1. 완전탐색? 
# 3. 2 번을 구분할 수 있으면, 단순히 계단마다 해당하는 사람을 큐에 넣으면된다. 


# 4. 사람의 수는 1 ~ 10 명 사이이고, 계단은 항상 두 개이다!!!

# 5. 걸리는 시간을 계산해보자. 
# a, b, c 가 1번 계단, d, e, f 가 2번 계단에 도착한다고 하자.
# 계단에 도착한 순서대로 
# IF 큐에 3명 보다 많은 경우 => 대기 해야함. 
# ELSE 큐에 3명 보다 적은 경우 => 바로 큐에 집어 넣는다. 
# a 가 계단에 도달하는 시간 + 계단을 내려가는 시간 
# 마지막 c 가 계단에 도달하는 시간 + 계단을 내려가는 시간

# 최종적으로, 남은 사람이 없고, 큐가 비게 되는 시간을 계산한다..?

