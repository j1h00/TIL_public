"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
"""
import sys

N = int(sys.stdin.readline())
A = list(map(int, input().split()))

dp = [1]*N

# 2중 for loop
for i in range(1, N):
    for j in range(i): # i 까지의 수들을 확인해서 
        if A[i] > A[j]: # 만약 i 번째 수가 j 번째 수보다 크다면
            dp[i] = max(dp[i], dp[j] + 1) # dp[i] 를 업데이트 한다.

print(max(dp))