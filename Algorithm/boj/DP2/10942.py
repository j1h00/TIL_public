"""
    명우는 홍준이와 함께 팰린드롬 놀이를 해보려고 한다.
    먼저, 홍준이는 자연수 N개를 칠판에 적는다. 그 다음, 명우에게 질문을 총 M번 한다.

    각 질문은 두 정수 S와 E(1 ≤ S ≤ E ≤ N)로 나타낼 수 있으며, 
    S번째 수부터 E번째 까지 수가 팰린드롬을 이루는지를 물어보며, 
    명우는 각 질문에 대해 팰린드롬이다 또는 아니다를 말해야 한다.
"""
import sys
input = sys.stdin.readline # 이 문제는, sys.stdin 사용 안할 시, 시간초과!! => input M 이 너무 많다..

N = int(input())
nums = list(map(int, input().split()))
# 미리 i ~ j 까지의 부분 문자열이 palindrom 인지 판별한 dp 배열을 생성한다. 
# dp[i][j] 의 palindrom 여부는, 
# 1. False if if nums[i] != nums[j] 
# 2. else, 
# 2-1. True if dp[i-1][j-1] == True
# 2-2. else, False 

dp = [[0]*N for _ in range(N)]
for l in range(N): # l 은 s 와 e 의 차이   
    for i in range(N-l):
        j = i + l
        if i == j: 
            dp[i][j] = 1

        elif nums[i] == nums[j]:
            if j - 1 == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i+1][j-1]

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])

            
            
        
        


