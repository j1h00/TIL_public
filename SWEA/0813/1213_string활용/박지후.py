import sys

sys.stdin = open('input.txt', encoding = 'UTF-8')

T = 10

for tc in range(1, T+1):
    tc = int(input())
    target = input()
    seq = input()

    cnt = 0
    temp = ''
    for c in seq:
        temp += c
        if temp[-len(target):] == target:
            cnt += 1

    print(f'#{tc} {cnt}')
