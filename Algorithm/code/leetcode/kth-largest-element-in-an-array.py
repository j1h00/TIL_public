# https://leetcode.com/problems/kth-largest-element-in-an-array/


from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        sorted_nums = sorted(nums, reverse=True)
        return sorted_nums[k-1]

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# short
def findKthLargest1(self, nums, k):
    return sorted(nums)[-k]
    

# heap
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(1, k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)

    # heapify 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)
    
    #nlargest
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


############ quick selection 
# O(n) time, quick selection
def findKthLargest(self, nums, k):
    # convert the kth largest to smallest
    return self.findKthSmallest(nums, len(nums)+1-k)
    
def findKthSmallest(self, nums, k):
    if nums:
        pos = self.partition(nums, 0, len(nums)-1)
        if k > pos+1:
            return self.findKthSmallest(nums[pos+1:], k-pos-1)
        elif k < pos+1:
            return self.findKthSmallest(nums[:pos], k)
        else:
            return nums[pos]
 
# choose the right-most element as pivot   
def partition(self, nums, l, r):
    low = l
    while l < r:
        if nums[l] < nums[r]:
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    nums[low], nums[r] = nums[r], nums[low]
    return low