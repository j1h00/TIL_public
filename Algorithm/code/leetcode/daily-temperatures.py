# https://leetcode.com/problems/daily-temperatures/
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # use nested for loop ??? => easy but time limmit exceeded 
        return 
        # use stack !!
        

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# How ? stack 에 index 를 쌓고, 
# 만약 stack[-1] 온도보다 현재 온도가 높다면, 
# answer[stack[-1]] 를 업데이트 한다. 

# for loop 을 한 번만 돌기 때문에 O(N) 으로 처리가 가능하다. 
# answer[i] 를 아직 모르는 상태에서, answer[i+10] 의 값을 먼저 찾을 수도 있다. 

# most viewed solution 
class Solution:
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T): # iterate forward 
            while stack and T[stack[-1]] < t: # stack[-1] 보다 현재 온도가 높다면 
                cur = stack.pop() 
                ans[cur] = i - cur # answer[stack[-1]] 업데이트 해준다. 
            stack.append(i)

        return ans


