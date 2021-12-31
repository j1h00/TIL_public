import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = sorted(list(map(int, input().split())))
    new_nums = []

    max_idx = N-1
    min_idx = 0
    for i in range(N//2):
        new_nums.append(nums[max_idx])
        new_nums.append(nums[min_idx])
        max_idx -= 1
        min_idx += 1

    print(f'#{tc}', end = " ")
    print(*new_nums[:10])