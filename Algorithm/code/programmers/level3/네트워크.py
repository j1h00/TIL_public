from collections import deque
# bfs 로 해결해보자 
def solution(n, computers):
    answer = 0

    visited = [0]*n
    for start in range(n):
        if visited[start]:
            continue

        answer += 1
        visited[start] = 1
        queue = deque([start])

        while queue:
            now = queue.popleft()

            for nxt in range(n):
                if not visited[nxt] and computers[now][nxt]:
                    queue.append(nxt)
                    visited[nxt] = 1

    return answer



answer1 = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
answer2 = solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])

print(answer1, answer2)