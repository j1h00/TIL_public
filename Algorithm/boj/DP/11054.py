"""
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.
수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.
"""
import sys

N = int(sys.stdin.readline())
A = list(map(int, input().split()))

def lis(A, N): # LIS(Longest Increasing Subsequence) 가장 긴 증가하는 부분 수열을 찾는다. 
    dp = [1]*N
    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

forward = lis(A, N)
backward = lis(A[::-1], N)[::-1] # 뒤집어서 LIS 찾은 뒤, 다시 뒤집는다. 
result = []
for i in range(N):
    result.append(forward[i] + backward[i])

print(max(result)-1)

"""
x = int(input())

case = list(map(int, input().split()))
reverse_case = case[::-1]

increase = [1 for i in range(x)] # 가장 긴 증가하는 부분 수열
decrease = [1 for i in range(x)] # 가장 긴 감소하는 부분 수열(reversed)

for i in range(x):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_case[i] > reverse_case[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for i in range(x)]
for i in range(x):
    result[i] = increase[i] + decrease[x-i-1] -1

print(max(result))
"""