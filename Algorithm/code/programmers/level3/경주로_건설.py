"""
    건설 비용을 계산해 보니 직선 도로 하나를 만들 때는 100원이 소요되며, 
    코너를 하나 만들 때는 500원이 추가로 듭니다.
    경주로를 건설하는데 필요한 최소 비용을 return
"""

# bfs, dfs 로 경로를 찾아서 모두 계산하자 
# 최소 경로를 구하는 문제이므로, 중간에 가지치기가 가능하다. 
# bfs 보다는, 한 경로를 끝까지 가는 dfs 가 비용 계산에 유리할 것 같다.
# !!!! 최단 경로 문제임을 잊었다. dfs 로 실행 시 너무 오래 걸린다. 


# 25 번 문제가 해결이 안된다. 이유를 모르겟다...
from collections import deque

def solution(board):
    n = len(board)
    cost_board = [[10**9]*n for _ in range(n)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    start = (0, 0, -1, 0)
    q = deque([start])
    cost_board[0][0] = 0
    while q:
        x, y, prev_d, prev_cost = q.popleft()
        for d in range(4):
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            cost = prev_cost + (100 if prev_d == d or prev_d == -1 else 600)
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny] and cost_board[nx][ny] >= cost - 5:
                cost_board[nx][ny] = cost
                q.append((nx, ny, d, cost))

    return cost_board[n-1][n-1]

answer1 = solution([[0,0,0],[0,0,0],[0,0,0]])
answer2 = solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
answer3 = solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
answer4 = solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])

print(answer1)
print(answer2)
print(answer3)
print(answer4)