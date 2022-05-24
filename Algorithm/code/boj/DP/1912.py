"""
n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 
단, 수는 한 개 이상 선택해야 한다.
"""
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

dp = [0] * N
dp[0] = nums[0]
for i in range(1, N):
    dp[i] = max(nums[i], dp[i-1] + nums[i]) # 이전까지의 합에 i 를 더한 것과, i 중에 큰 것을 고른다.  

print(max(dp))