"""
    배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 
    서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. 
    예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다. 
    0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.
"""
import sys
from collections import deque

def bfs(graph, a, b):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(graph)
    m = len(graph[0])
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny]:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                count += 1
    return count 


def main():
    T = int(sys.stdin.readline())
    for i in range(T): 
        M, N, K= map(int, sys.stdin.readline().split())

        field = [[0 for i in range(M)] for i in range(N)]
        for i in range(K):
            c, r, = map(int, sys.stdin.readline().split())
            field[r][c] = 1
        
        result = []
        for i in range(N):
            for j in range(M):
                if field[i][j]:
                    result.append(bfs(field, i, j))

        print(len(result))
main()

