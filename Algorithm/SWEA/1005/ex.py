# 1. 배열의 데이터를 퀵 정렬하는 함수를 작성하고 테스트 해보시오.​
# ​입력 예​
# [11, 45, 23, 81, 28, 34​]
# [11, 45, 22, 81, 23, 34, 99, 22, 17, 8​]
# [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# 2. [1,2,3,4,5,6,7,8,9,10]의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.


def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[0]
    left, right = [], []

    for number in nums[1:]:
        if number < pivot:
            left.append(number)
        else:
            right.append(number)

    return quick_sort(left) + [pivot] + quick_sort(right)
    