# https://leetcode.com/problems/product-of-array-except-self/
from typing import List

# the product of all the elements of nums except nums[i].
# 배열에서 자기 자신을 제외한 모든 요소들의 곱 
# 
# condition 
# 1. O(n)
# 2. without using the division operation.

# answer[i] 를 구하고 싶으면, 
# [0, i-1] 과 [i+1, -1] 의 모든 요소의 곱을 곱하면 된다. 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 배열을 2개 사용하는 방법 
        n = len(nums)

        forward = [1]        
        for i in range(n-1):
            forward.append(forward[-1] * nums[i])
        
        backward = [1]
        for j in range(n-1, 0, -1):
            backward.append(backward[-1] * nums[j])

        answer = []
        for k in range(n):
            answer.append(forward[k] * backward[n-1 - k])
        return answer
        
#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# using ONE array 
class Solution:
        # @param {integer[]} nums
        # @return {integer[]}
        def productExceptSelf(self, nums):
            n = len(nums)
            output = []

            p = 1
            for i in range(0,n): # forward
                output.append(p)
                p = p * nums[i]

            p = 1
            for i in range(n-1,-1,-1): # backward
                output[i] = output[i] * p
                p = p * nums[i]
            return output