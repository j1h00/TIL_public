import sys

sys.stdin = open("input.txt")

T = int(input())

def quick_sort(nums, p, r):
    if p < r:
        q = partition(nums, p, r)
        quick_sort(nums, p, q-1)
        quick_sort(nums, q+1, r)

def partition(nums, p, r):
    x = nums[r]
    i = p-1
    for j in range(p, r):
        if nums[j] < x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i+1

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    quick_sort(nums, 0, N-1)

    print(f'#{tc}', end = " ")
    print(*nums)