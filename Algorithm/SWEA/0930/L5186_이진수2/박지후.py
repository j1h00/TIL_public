import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = float(input())

    cnt = -1
    answer = ""
    while N > 0:
        if N >= 2**cnt:
            N -= 2**cnt
            print(N)
            answer += "1"
        else:
            answer += "0"
        cnt -= 1
    
    if N == 0 and cnt >= -13:
        print(f'#{tc} {answer}')
    else:
        print(f'#{tc} overflow')
        