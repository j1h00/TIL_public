import sys
sys.stdin = open('input.txt')


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    merged = merge(left, right) 

    return merged


def merge(left, right):
    global cnt 

    i, j = 0, 0
    merged = []
    if left[-1] > right[-1]:
        cnt += 1
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1
    if i < len(left):
        merged.extend(left[i:])
    elif j < len(right):
        merged.extend(right[j:])

    return merged

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    a = list(map(int, input().split()))
    cnt = 0

    sorted_a = merge_sort(a)

    print(f'#{tc} {sorted_a[len(a)//2]} {cnt}')