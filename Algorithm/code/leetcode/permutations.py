# https://leetcode.com/problems/permutations/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        N = len(nums)
        answer = []
        self.dfs(nums, [], N, answer)
        return answer

    def dfs(self, nums, visited, N, answer):
        if len(visited) == N:
            answer.append(visited)

        for num in nums:
            if num not in visited:
                self.dfs(nums, visited + [num], N, answer)
    
        
#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# pythonic 
import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))

# recursive (use slicing)
def permute(self, nums):
    res = []
    self.dfs(nums, [], res)
    return res
    
def dfs(self, nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    for i in range(len(nums)):
        self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

# recursive (use remove) 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return 