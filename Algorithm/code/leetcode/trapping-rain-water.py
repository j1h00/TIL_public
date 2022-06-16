# https://leetcode.com/problems/trapping-rain-water/

from typing import List

# failed => [4, 2, 3] 
# 무조건 left 보다 높은 경우를 찾으므로, 위 경우는 찾지 못한다. 
class Solution:
    def trap(self, height: List[int]) -> int:
        
        N = len(height)
        answer = 0 
        i = 0 if height[0] else 1
        while i < N:
            left = height[i]
            trapped = 0
            flag = False
            for j in range(i+1, N):
                right = height[j]
                if right >= left:
                    answer += trapped
                    flag = True
                    break
                else:
                    trapped += left - right
            
            if flag:
                i = j 
            else:
                i += 1

        return answer
        
#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

