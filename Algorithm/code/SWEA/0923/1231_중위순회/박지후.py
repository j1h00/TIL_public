import sys
sys.stdin = open('input.txt')

def inorder(n):
    if val[n]:
        inorder(left[n])
        print(val[n], end = "") # 중위 순회하면서, 노드가 가진 알파벳을 출력합니다. 
        inorder(right[n])


T = 10
for tc in range(1, T+1):
    N = int(input())

    left = [0] * (N+1)
    right = [0] * (N+1)
    val = [0] * (N+1)
    for i in range(N):
        info = input().split()
        while len(info) < 4:
            info.append(0)
        idx, a, l, r = info # 입력을 받습니다.
        idx, l, r = map(int, [idx, l, r]) # integer 로 변환합니다. 
        val[idx] = a
        left[idx] = l
        right[idx] = r

    print(f'#{tc}', end = " ")
    inorder(1) # 중위 순회합니다!
    print() 
    