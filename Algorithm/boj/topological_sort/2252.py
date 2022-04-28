# 위상정렬

from collections import deque


N, M = map(int, input().split())

in_degree = [0] * (N + 1)
after = { k:[] for k in range(1, N+1) } 

for _ in range(M):
    A, B = map(int, input().split())
    after[A].append(B)
    in_degree[B] += 1

q = deque()
for i in range(1, N+1):
    if not in_degree[i]:
        q.append(i)

answer = []
while q:
    now = q.popleft()
    answer.append(now)

    for nxt in after[now]:
        in_degree[nxt] -= 1
        if not in_degree[nxt]:
            q.append(nxt)


for i in answer:
    print(i, end=" ")

            
    
