import sys
sys.stdin = open('input.txt')


def inorder(n):
    global cnt 
     
    if n < N+1:
        inorder(2*n)
        tree[n] = nums.pop() 
        inorder(2*n + 1)
        

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    tree = [0] * (N+1)
    nums = list(range(N, 0, -1)) # 노드에 넣어줄 값들의 리스트
    
    inorder(1) # 중위 순회를 하면서 노드에 값을 넣어줍니다. 

    print(f'#{tc} {tree[1]} {tree[N//2]}')
    