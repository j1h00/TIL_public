import sys
sys.stdin = open('input.txt')


def quick_sort(p, r):
    if p < r:
        q = partition(p, r)
        quick_sort(p, q-1)
        quick_sort(q+1, r)

# Lomuto partition
def partition(p, r):
    x = nums[r] # pivot, 이 경우엔 가장 오른쪽 수를 기준으로 잡는다. 
    i = p-1 # swap 기준선

    for j in range(p, r): # 배열의 수를 하나씩 확인하면서 
        if nums[j] < x: # pivot 인 x 보다 작은 경우 
            i += 1
            nums[i], nums[j] = nums[j], nums[i] # swap 해준다. 

    nums[i+1], nums[r] = nums[r], nums[i+1] # pivot 과 경계에 있는 수를 교환 
    return i+1

    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 리턴 값 없이 nums 를 참조하여 정렬. 
    quick_sort(0, N-1)

    print(f'#{tc} {nums[N//2]}')