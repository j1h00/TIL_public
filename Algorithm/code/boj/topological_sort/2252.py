# 위상정렬

from collections import deque


N, M = map(int, input().split())

in_degree = [0] * (N + 1) # i 로 가기 전 거쳐야하는 노드의 수
after = { k:[] for k in range(1, N+1) } # k 이후에 갈 수 있는 노드의 배열

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
    answer.append(now) # 방문 

    for nxt in after[now]: 
        in_degree[nxt] -= 1
        if not in_degree[nxt]: # nxt 로 가기 전 거쳐야 하는 노드가 없다면
            q.append(nxt) # 방문 큐에 추가 


for i in answer:
    print(i, end=" ")

            
    
