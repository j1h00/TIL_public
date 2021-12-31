"""
    수빈이는 동생과 숨바꼭질을 하고 있다. 
    수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
    수빈이는 걷거나 순간이동을 할 수 있다. 
    만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
    순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

    수빈이와 동생의 위치가 주어졌을 때, 
    수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
"""
# 1697 숨바꼭질 문제 변형 => 이동 경로도 출력해야 함. 
# how?
# 1. 경로 저장 => 메모리 초과 
# 2. traceback => 성공 
# 3. 배열을 하나 만들어서, 지나온 바로 직전 노드 저장.
from collections import deque

N, K = map(int, input().split())

q = deque()
q.append(N)

visited = [0]*(100001)
visited[N] = 1
while q:
    now = q.popleft()
    if now == K:
        print(visited[now] - 1)
        break 

    for nxt in [now-1, now+1, now*2]:
        if 0 <= nxt <= 100000 and not visited[nxt]:
            q.append(nxt)
            visited[nxt] = visited[now] + 1

now = K
cnt = visited[K] - 1

# 2번 방법
answer = [K]
while now != N:
    for prev in [now-1, now+1, now//2]:
        if 0 <= prev <= 100000 and visited[prev] == cnt:
            now = prev
            cnt -= 1
            answer.append(now)
            break 

print(*answer[::-1])
    