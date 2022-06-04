# https://leetcode.com/problems/number-of-islands/


from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid = [list(map(int, row)) for row in grid]
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        n, m = len(grid), len(grid[0])
        visited = [[0] * m for _ in range(n)]

        def bfs (i, j, grid, n, m):
            q = deque([(i, j)])
            visited[i][j] = 1
        
            while q:
                x, y = q.popleft()
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy 
                    
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = 1

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] and not visited[i][j]:
                    count += 1
                    bfs(i, j, grid, n, m)

        return count