def preorder_traverse(N):  # 전위 순회
    global count_nodes
    if N:  # N != 0 일때
        count_nodes += 1  # 유효한 정점이니 +1
        preorder_traverse(left[N])  # 왼쪽 자식 노드 확인
        preorder_traverse(right[N])  # 오른쪽 자식 노드 확인


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    left = [0] * (E+2)  # 왼쪽 자식 노드
    right = [0] * (E+2)  # 오른쪽 자식 노드
    edge = list(map(int, input().split()))
    for i in range(E):
        if left[edge[2*i]] == 0:  # 왼쪽 자식 노드가 없으면
            left[edge[2*i]] = edge[2*i+1]
        else:  # 왼쪽 자식 노드가 있으면
            right[edge[2*i]] = edge[2*i+1]

    count_nodes = 0  # 서브 트리 노드의 수 계산 
    preorder_traverse(N)
    print(f'#{tc} {count_nodes}')