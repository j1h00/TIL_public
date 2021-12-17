import sys
sys.stdin = open('input.txt')
import heapq


# 최소 비용, 최단 경로 문제 
def dijkstra():
    distance = [[float('inf')]*N for _ in range(N)] # 그 곳까지 도달하는 데 필요한 비용을 저장 
    heap = [(0, (0, 0))] # (0,0) 에서 시작 
    distance[0][0] = 0

    while heap:
        w, now = heapq.heappop(heap)
        x, y = now[0], now[1] # 현재 위치 

        if distance[x][y] < w: 
            # 지금 경로로 (x,y) 까지 도달하는데 필요한 비용이, 다른 경로보다 이미 더 큰 경우
            # => heapq 를 사용하다 보니, 동일한 노드라도 큐에 저장이 될 수 있어서 처리해준다.  
            continue

        for dx, dy in directions: # 4 방향 모두 탐색 
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N: 
                plus = 0 # 높이에 따른 추가 비용 
                if arr[nx][ny] > arr[x][y]:
                    plus = arr[nx][ny] - arr[x][y]
                nw = w + 1 + plus # 다음 위치로 가는 데 필요한 비용 
                if distance[nx][ny] > nw: # 비용 비교하여 최소 경로를 남김.  
                    distance[nx][ny] = nw 
                    heapq.heappush(heap, [nw, (nx, ny)])

    return distance[N-1][N-1]

# 최소 비용 문제 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    start = (0,0)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    print(f'#{tc} {dijkstra()}')