# https://leetcode.com/problems/array-partition-i/submissions/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort() 
        answer = 0
        for i in range(len(nums)// 2):
            answer += nums[2 * i] 

        return answer

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# short 
class Solution(object):

    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])