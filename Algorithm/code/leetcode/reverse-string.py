# https://leetcode.com/problems/reverse-string/

# Conditions
# 1. in-place https://en.wikipedia.org/wiki/In-place_algorithm
# 2. O(1)

from typing import List

# wrong
class Solution:
    def reverseString(self, s: List[str]) -> None:
        last_idx = len(s) - 1
        for i in range(last_idx // 2):
            target = last_idx - i
            s[i], s[target] = s[target], s[i] 
        
        print(s)

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# two pointer 
class Solution:
    def reverseString(self, s):
        for i in range(len(s)//2): s[i], s[-i-1] = s[-i-1], s[i]  
        
# pythonic 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
        # Not ` s = s[::-1] `
        # Under the hood, s[:] = is editing the actual memory bytes s points to, 
        # and s = points the variable name s to other bytes in the memory.