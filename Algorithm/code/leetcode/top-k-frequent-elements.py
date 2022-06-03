# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List


# time complexity <= O(n log n) 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1

        counts = sorted(list(num_counts.keys()), key= lambda x: num_counts[x], reverse = True)
        return counts[:k]

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# https://leetcode.com/problems/top-k-frequent-elements/discuss/740374/Python-5-lines-O(n)-buckets-solution-explained.
# use bucket sort 
from collections import Counter
from itertools import chain

class Solution:
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()  
        for num, freq in Count: bucket[freq].append(num) # bucket 에 담는다. 
        flat_list = list(chain(*bucket)) # 하나의 list 로 flatten
        return flat_list[::-1][:k]