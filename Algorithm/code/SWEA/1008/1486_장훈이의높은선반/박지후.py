import sys
sys.stdin = open('input.txt')


def dfs(i, H_acc, visit, N, B):
    global answer

    if H_acc >= B and H_acc < answer:
        answer = H_acc
        return 

    for idx in range(i, N):
        if not visit & ( 1 << idx ):
            dfs(idx+1, H_acc + H[idx], visit | ( 1 << idx ), N, B)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())

    H = list(map(int, input().split()))

    answer = float('inf')
    dfs(0, 0, 0, N, B)

    print(f'#{tc} {answer - B}')
    