from collections import deque

# 위상 정렬을 이용한 풀이
# initialize 
N = int(input())

in_degree = [0] * (N+1)
time = [0] * (N+1)
build_after = { k:[] for k in range(1, N+1) } # k 가 있을 때, 지을 수 있는 건물
q = deque() # queue for topological sort

for a in range(1, N+1):
    info = input().split()
    time[a] = int(info[0])
    for b in info[1:]:
        if b == "-1":
            break 
        else:
            build_after[int(b)].append(a)
            in_degree[a] += 1

    if not in_degree[a]:
        q.append(a)

# topological sort
result = [0] * (N+1)

while q:
    now = q.popleft()

    result[now] += time[now]
    for b in build_after[now]:
        in_degree[b] -= 1

        # 걸리는 최소 시간.. 만약 now 가 아니라 다른 선수 건물이 있는 경우, 
        # 그 선수 건물을 만들기까지 더 오래걸린다면 ?
        result[b] = max(result[b], result[now]) 
        if not in_degree[b]:
            q.append(b)

for answer in result[1:]:
    print(answer)

    


# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1