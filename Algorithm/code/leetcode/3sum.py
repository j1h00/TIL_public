# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2): 
            if i > 0 and nums[i] == nums[i-1]: # i != j 조건 만족 
                continue
                
            l, r = i+1, len(nums)-1 # i 이후의 모든 경우의 수에 대해 two pointer 
            while l < r: 
                s = nums[i] + nums[l] + nums[r]
                if s < 0: # 0 보다 작은 경우, 더 큰 수를 선택. 
                    l +=1 
                elif s > 0: # 0 보다 큰 경우, 더 작은 수를 선택
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    
                    # 중복 제거를 위한 코드 
                    # 위에서 이미 l 이 선택 되었는데, 다음 loop 에서 같은 값의 l+1 이 선택되면 안됨
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
