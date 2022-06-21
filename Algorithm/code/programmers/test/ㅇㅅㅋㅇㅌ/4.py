min_camp = 10 ** 6

def solution(grid, k): 
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    n, m = len(grid), len(grid[0])

    visited = [[0] * m for _ in range(n)]
    def backtrack(now, power, camp):
        global min_camp

        if camp > min_camp: # 이미 최소 야영 횟수를 넘은 경우,
            return 

        x, y = now 
        if x == n-1 and y == m-1 and camp < min_camp: # 목적지에 도착했고, 현재 야영 횟수가 최소 야영 횟수보다 적은 경우 
            min_camp = camp 
            return 

        if not power: # 이동 가능한 횟수를 모두 사용한 경우
            return 
   
        for dx, dy in directions: # 상하좌우 4개 방향에 대해 
            nx, ny = x + dx, y + dy 
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#' and not visited[nx][ny]: # 강이 아니고, 방문하지 않은 경우 
                visited[nx][ny] = 1 

                if grid[nx][ny] == '.': # 평지인 경우 
                    backtrack((nx, ny), power + 4, camp + 1) # 야영을 하는 경우, 이동 가능 횟수 초기화, 야영 횟수 증가.  

                backtrack((nx, ny), power - 1, camp) # 야영을 하지 않는 경우, 이동 가능 횟수 감소.

                visited[nx][ny] = 0
        return 

    backtrack((0, 0), k, 0) # 시작 지점에서 시작

    return min_camp 