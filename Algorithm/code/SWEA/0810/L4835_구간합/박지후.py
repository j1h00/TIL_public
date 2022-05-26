import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = map(int, input().split())

    acc_list = []
    acc = 0
    for num in num_list:
        acc += num
        acc_list.append(acc)

    max_sum = acc_list[M-1]
    min_sum = acc_list[M-1]
    start = 1
    end = M
    while end != N:
        now_sum = acc_list[end] - acc_list[start-1]
        if max_sum < now_sum:
            max_sum = now_sum
        if min_sum > now_sum:
            min_sum = now_sum
        start += 1
        end += 1

    print(f'#{tc} {max_sum - min_sum}')