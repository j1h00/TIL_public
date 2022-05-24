#원래 i번째 물약의 가격은 동전 c_i개이다. 만약 i번째 물약을 구매하면, p_i종류의 다른 물약의 가격이 내려간다.

from collections import deque

def main():
    N = int(input())
    cost = [0] + list(map(int, input().split()))

    discount = {k:[] for k in range(1, N+1)}
    total_discount = {k:0 for k in range(1, N+1)}
    for i in range(1, N+1):
        p = int(input())
        for j in range(p):
            a, d = map(int, input().split())
            actual_d = d if cost[a] > d else cost[a] - 1
            discount[i].append((a, actual_d))
            total_discount[i] += actual_d

    sorted_discount = sorted(total_discount.items(), key=lambda x: x[1], reverse=True)

    total_cost = 0
    visited = [0] *(N+1)

    q = deque([sorted_discount[0][0]])
    visited[1] = 1
    while q:
        now = q.popleft()
        total_cost += cost[now]
        for nxt, dis in discount[now]:
            if not visited[nxt]:
                q.append(nxt)
                temp = cost[nxt] - dis 
                cost[nxt] = temp if temp > 0 else 1
                visited[nxt] = 1
    
    print(total_cost)

main()