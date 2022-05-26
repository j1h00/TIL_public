import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) // 10 

    case_acc = [0]*N
    case_acc[0] = 1
    case_acc[1] = 3
    for i in range(2, N):
        case_acc[i] = case_acc[i-2] * 2 + case_acc[i-1]

    answer = case_acc[-1]
    print(f'#{tc} {answer}')
