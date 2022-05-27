# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        cur_min = prices[0]
        acc = []
        for i in range(n):
            if prices[i] < cur_min:
                cur_min = prices[i]
            acc.append(cur_min)

        cur_max = prices[n-1]
        for i in range(n-1, -1, -1):
            if prices[i] > cur_max:
                cur_max = prices[i]
            acc[i] = prices[i] - acc[i]

        return max(acc)


#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#


# while loop with two pointer 
class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit


# for loop
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfitOptimal(prices)
    
        # return self.maxProfitByTwoLoops(prices)
    
#     O(n) || O(1) 1778ms 15.94%
    def maxProfitOptimal(self, prices):
        if not prices:
            return 0
        minVal = prices[0]
        maxVal = float('-inf')
        
        for i in range(1, len(prices)):
            profit = prices[i] - minVal
            maxVal = max(maxVal, profit)
            minVal = min(minVal, prices[i])
            
        return maxVal if maxVal > 0 else 0
    
#     O(N^2) || O(1) TLE
    def maxProfitByTwoLoops(self, prices):
        if not prices:
            return prices
        
        maxVal = float('-inf')
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                maxVal = max(maxVal, prices[j] - prices[i])
        
        return maxVal if maxVal > 0 else 0