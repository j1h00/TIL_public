import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    num, max_swap = input().split()
    num = [i for i in num]
    max_swap = int(max_swap)

    N = len(num)
    cnt = 0
    for i in range(N):
        MAX_idx = i
        for j in range(N-1, i, -1):
            if num[MAX_idx] < num[j]:
                MAX_idx = j
        if MAX_idx != i:
            num[i], num[MAX_idx] = num[MAX_idx], num[i]
            cnt += 1
            print(num)
        if cnt == max_swap:
            break

    remain = max_swap - cnt
    print(max_swap, cnt, remain)
    if not remain:
        pass
    elif remain % 2:
        pass
    else:
        num[-1], num[-2] = num[-2], num[-1]
    answer = ''.join(num)
    print(f'#{tc} {answer}')