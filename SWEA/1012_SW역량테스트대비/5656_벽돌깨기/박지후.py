import sys
sys.stdin = open('input.txt')
from collections import deque


def go(cnt, arr):
    global result

    if (cnt == N): # N 번 실행한 뒤엔 
        result = min(result, get_remain(arr)) # 남아있는 벽돌 개수 세기 
        return 

    for j in range(W): # 모든 열에 대하여 구슬을 떨어뜨릴 예정. 
        # 구슬에 맞는 벽돌을 찾는다. 
        top = -1 
        for i in range(H):
            if arr[i][j]:
                top = i
                break
        if top == -1: # 벽돌이 하나도 없다면 
            go(cnt + 1, arr) # 다음 구슬 
        else: # 벽돌이 있다면 
            new_arr = [row[:] for row in arr] # arr 복사 
            boom(new_arr, top, j) # 벽돌 제거 
            down(new_arr) # 벽돌 내리기 
            go(cnt + 1, new_arr) # 다음 구슬 떨어뜨리기 


def get_remain(arr): # 남아있는 벽돌의 개수를 세는 함수 
    total = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j]: # 0 이 아니면 
                total += 1 # 갯수 추가 
    return total


def boom(arr, i, j): # 벽돌 제거 함수 
    queue = deque() # BFS 탐색으로 제거 

    if arr[i][j] > 1: # 1 인 경우, 자기 자신만 제거되므로. 큐에 추가 하지 않는다. 
        queue.append((i,j, arr[i][j])) # arr[i][j] 를 들고 다닌다. (상하좌우 몇개 깨야할 지 알아야함)
    arr[i][j] = 0 # 제거한 벽돌은 0 으로 변경

    while queue:
        x, y, cnt = queue.popleft() 
        for dx, dy in directions: # 4개 방향에 대해서 
            nx = x
            ny = y
            for _ in range(cnt-1): # 벽돌에 적힌 숫자만큼 이동을 반복
                nx += dx
                ny += dy 
                if 0 <= nx < H and 0 <= ny < W and arr[nx][ny]: # 범위 안에 있고, 벽돌이 0 이 아니면 
                    if arr[nx][ny] > 1: # 1인 경우, 자기 자신만 제거되므로 큐에 추가하지 않음. 
                        queue.append((nx, ny, arr[nx][ny])) # 큐에 추가 
                    arr[nx][ny] = 0 # 0 으로 변경 

def down(arr):
    tmp = deque()
    for j in range(W):
        for i in range(H-1, -1, -1): # 밑에서 부터 돌면서 
            if arr[i][j]: # 0 이 아니면 
                tmp.append(arr[i][j]) # tmp 에 추가 
                arr[i][j] = 0 # 0 으로 변경 

        k = H-1 # 마찬가지로 밑에서부터 
        while tmp: # tmp 에 있는 값들을 하나씩 채워나감 
            arr[k][j] = tmp.popleft()
            k -= 1 

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())

    origin_arr = []
    for _ in range(H):
        origin_arr.append(list(map(int, input().split())))
    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = float('inf') 

    go(0, origin_arr)
    print(f'#{tc} {result}')
