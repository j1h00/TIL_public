import sys

sys.stdin = open("input.txt")

T = int(input())

def binary_search(target, left, right):
    cnt = 0
    while left <= right:
        mid = (left + right) // 2
        cnt += 1
        if target == mid:
            return cnt
        elif target < mid:
            right = mid
        else:
            left = mid

    return cnt

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    left = 1
    right = P
    A = binary_search(Pa, left, right)
    B = binary_search(Pb, left, right)

    win = 'A'
    if A == B:
        win = 0
    elif A > B:
        win = 'B'

    print(f'#{tc} {win}')