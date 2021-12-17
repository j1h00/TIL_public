import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    
    tree = [0] * (N+1)
    for i in range(M):
        leaf_n, value = map(int, input().split())
        tree[leaf_n] = value

    for i in range(N, -0, -1): # 가장 아래에 있는 노드에서부터 시작하여 자식 노드의 값을 부모에 더해줍니다.
        left, right = i*2, i*2 + 1
        if left <= N: # 왼쪽에 자식이 존재하면 
            tree[i] += tree[left]  
        if right <= N: # 오른쪽에 자식이 존재하면
            tree[i] += tree[right] 

    print(f'#{tc} {tree[L]}')
    