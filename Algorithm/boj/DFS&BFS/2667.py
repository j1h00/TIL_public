from collections import deque

def bfs(arr, a, b): # bfs 
    queue = deque([(a,b)])
    arr[a][b] = 0 # 이미 왔던 곳은 0 으로 변경 
    cnt = 1 # 도달가능한 위치의 수 

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions: # 
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny]:
                queue.append((nx,ny))
                arr[nx][ny] = 0
                cnt += 1 # 

    return cnt 

directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input())))

answer = []
for i in range(N):
    for j in range(N): 
        if arr[i][j]: # 시작점을 찾아서 
            answer.append(bfs(arr, i, j)) # bfs 탐색 후, 도달 가능한 위치의 수를 answer 에 저장 

answer.sort()
print(len(answer))
for i in answer:
    print(i)