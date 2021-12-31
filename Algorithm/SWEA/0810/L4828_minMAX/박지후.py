import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    min = max = num_list[0]
    for now_num in num_list:
        if now_num > max:
            max = now_num
        if now_num < min:
            min = now_num

    print(f'#{tc} {max - min}')