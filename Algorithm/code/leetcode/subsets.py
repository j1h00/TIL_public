# https://leetcode.com/problems/subsets/

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        N = len(nums)
        for i in range(1 << N):
            subset = []
            for j in range(N):
                if i & 1 << j:
                    subset.append(nums[j])
            answer.append(subset)

        return answer

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# Iteratively 
def subsets(self, nums):
    res = [[]]
    for num in nums:
        res += [item+[num] for item in res]
    return res

# dfs 
def subsets(self, nums):
    ret = []
    self.dfs(nums, [], ret)
    return ret

def dfs(self, nums, path, ret):
    ret.append(path)
    for i in range(len(nums)):
        self.dfs(nums[i+1:], path+[nums[i]], ret)