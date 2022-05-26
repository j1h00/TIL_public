import sys
sys.stdin = open('input.txt')
import heapq


def dijkstra(): 
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    distance = [[float('inf')]*N for _ in range(N)]
    heap = [(0, (0,0))]
    distance[0][0] = 0

    while heap:
        w, now = heapq.heappop(heap)
        x, y = now

        if distance[x][y] < w:
            continue

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and distance[nx][ny] > w + arr[nx][ny]:
                distance[nx][ny] = w + arr[nx][ny] 
                heapq.heappush(heap, (distance[nx][ny], (nx,ny)))

    return distance[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input())))
   
    print(f'#{tc} {dijkstra()}')