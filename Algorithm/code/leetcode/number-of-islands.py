# https://leetcode.com/problems/number-of-islands/


from typing import List
from collections import deque

# bfs 
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

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# most viewed => dfs
def numIslands(self, grid):
    if not grid:
        return 0
        
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                self.dfs(grid, i, j)
                count += 1
    return count

def dfs(self, grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '#'
    self.dfs(grid, i+1, j)
    self.dfs(grid, i-1, j)
    self.dfs(grid, i, j+1)
    self.dfs(grid, i, j-1)


# bfs
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0   
        count = 0
        check = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =='1' and check[i][j]== False:
                    count += 1
                    self.search(grid,check,i,j)
        return count       
    def search(self,grid,check,i,j):
        qu = deque([(i,j)])
        while qu:
            i, j = qu.popleft()
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=='1' and check[i][j]==False:
                check[i][j] = True
                qu.extend([(i-1,j),(i+1,j),(i,j-1),(i,j+1)])