"""
    트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다.
    트리의 지름을 구하는 프로그램을 작성하시오.
"""
# 다익스트라로 모든 정점 사이의 거리를 찾아서 구하려고 했으나 실패!
# 1167_2.py 에선 BFS 를 사용해보자 
# 시간초과 실패!
# => 트리의 지름은 아무 노드에서 bfs 를 통해 가장 멀리있는 노드를 구한 후, 
#    해당 노드에서 bfs 를 한번 더 진행하여 가장 멀리 있는 노드를 구하면 된다!!!
# https://blog.myungwoo.kr/112 
# 아래와 같이 수정 
from collections import deque
INF = 10**9

def bfs(s, N):
    visited = [0]*(N+1)
    visited[s] = 1

    q = deque()
    q.append(s)
    while q:
        now = q.popleft()

        for nxt, nxt_d in graph[now]:
            if not visited[nxt]:
                visited[nxt] = visited[now] + nxt_d
                q.append(nxt)

    return visited

N = int(input())

graph = {v:[] for v in range(1, N+1)}

for i in range(N):
    info = list(map(int, input().split()))
    for j in range((len(info)-2)//2):
        graph[info[0]].append((info[2*j+1], info[2*j+2])) # 입력 받기 

answer = 0
tree_distance_from_one = bfs(1, N) # bfs 를 한 번 실행하여 1에서 부터 가장 먼 정점을 찾은 뒤
max_from_one = (0, 0) # 그 정점으로부터 가장 멀리 떨어진 정점을 찾는다. 
for i in range(N+1):
    if tree_distance_from_one[i] > max_from_one[1]:
        max_from_one = (i, tree_distance_from_one[i])
answer = max(bfs(max_from_one[0], N))

print(answer-1) # visited 에 처음 정점을 1 로 표시했기 때문에 -1 해줘야함. ㅠ

