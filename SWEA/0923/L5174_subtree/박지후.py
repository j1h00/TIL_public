import sys
sys.stdin = open('input.txt')

def preorder(n):
    if n: # n 이 0 이 아닌경우. 
        result.append(n) 
        preorder(left[n]) # 자식 노드가 없는 경우 0 이 전달
        preorder(right[n])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))

    left = [0]*(E+2) # 노드 번호는 1번부터 E+1번 까지 존재한다. 
    right = [0]*(E+2)  
    for i in range(E): # 입력을 받아 left, right child 노드 번호를 저장합니다.
        p = edges[2*i]
        c = edges[2*i + 1]
        if left[p]:
            right[p] = c
        else:
            left[p] = c

    result = []
    preorder(N) # N 을 시작으로 하여 순회합니다. 
    print(f'#{tc} {len(result)}') # 순회한 결과의 길이를 출력합니다.


