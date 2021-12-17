import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_seq = map(int, input())
    count = [0] * 10
    for num in num_seq:
        count[num] += 1

    max_card = 0
    max_cnt = 0
    for i in range(10):
        if count[i] >= max_cnt:
            max_cnt = count[i]
            max_card = i

    print(f'#{tc} {max_card} {max_cnt}')


