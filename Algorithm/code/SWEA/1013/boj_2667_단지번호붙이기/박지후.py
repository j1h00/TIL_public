from collections import deque

def bfs(arr, a, b): # bfs 
    queue = deque([(a,b)])
    arr[a][b] = 0 # 이미 왔던 곳은 0 으로 변경 
    count = 1 # 도달가능한 위치의 수 

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions: # 
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny]: # 범위 내에 ㅇ
                queue.append((nx,ny))
                arr[nx][ny] = 0
                count += 1

    return count 

directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input())))
print(arr)
cnt = []
for i in range(N):
    for j in range(N): 
        if arr[i][j]: # 시작점을 찾아서 
            cnt.append(bfs(arr, i, j)) # bfs 탐색 후, 도달 가능한 위치의 수를 cnt 에 저장 

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)