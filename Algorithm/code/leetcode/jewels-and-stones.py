# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        stoneDict = {}
        for stone in stones:
            if stoneDict.get(stone, 0):
                count += 1
                continue 
                
            if stone in jewels:
                count += 1
                stoneDict[stone] = 1
        
        return count

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# pythonic (using sum)
class Solution:
    def numJewelsInStones(self, J, S):
            setJ = set(J)
            return sum(s in setJ for s in S)