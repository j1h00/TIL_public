"""
    여행을 떠난 세준이는 지도를 하나 구하였다. 이 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다.
    한 칸은 한 지점을 나타내는데 각 칸에는 그 지점의 높이가 쓰여 있으며, 각 지점 사이의 이동은 지도에서 상하좌우 이웃한 곳끼리만 가능하다.
    현재 제일 왼쪽 위 칸이 나타내는 지점에 있는 세준이는 제일 오른쪽 아래 칸이 나타내는 지점으로 가려고 한다. 
    그런데 가능한 힘을 적게 들이고 싶어 항상 높이가 더 낮은 지점으로만 이동하여 목표 지점까지 가고자 한다. 

    지도가 주어질 때 이와 같이 제일 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 
    항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성하시오.
"""
from pprint import pprint 
import sys
sys.setrecursionlimit(10000) # as maximum height is 10000 => 최대 재귀 깊이가 10000

def dfs(now):
    x, y = now
    if x == N-1 and y == M-1: # 오른쪽 아래에 도착한 경우 
        return 1 # 경로를 하나 찾은 것이므로, 1을 리턴

    if dp[x][y] != -1: # 만약 처음 온 길이 아니라면 
        return dp[x][y] # 여기서 도착점 까지의 경로의 개수 dp[x][y] 를 리턴 

    dp[x][y] = 0
    for dx, dy in d: # 모든 방향에 대하여 
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] < arr[x][y]: # 만약 범위 내에 있고, 내리막길인 경우 
            dp[x][y] += dfs((nx, ny)) # dfs 로 탐색하여, (nx, ny) 에서 도착점 까지의 경로의 개수를 dp[x][y] 에 더해준다. 
    
    return dp[x][y] # (x, y) 에서 도착점 까지의 경로의 개수를 리턴한다!!! 

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
# 1. dfs or bfs
# 단순 dfs => 시간초과 => 한번 갔던 길도 또 다시 확인해야 하므로.. 
# Memoization => dp 를 이용해서 갔던 길은 경로가 몇개 존재하는지 적어두자! 두 번 가는 번거로움을 없애자

d = [(1, 0), (0, 1), (0, -1), (-1, 0)]
dp = [[-1]*M for _ in range(N)]

dfs((0, 0))
print(dp[0][0])