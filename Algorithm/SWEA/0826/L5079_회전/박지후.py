import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    # N 개의 수로 이루어진 수열은, 작업을 N 번 했을 때 제자리로 돌아옵니다. 
    M_left = M % N 
    answer = nums[M_left] # 남은 작업 수 만큼만 이동하면 되므로, 다음과 같습니다. 

    print(f'#{tc} {answer}') 