import sys

N = int(sys.stdin.readline())

dp = [0]*(N+1)

# 반대로 1에서부터 N까지 최소 연산의 횟수를 구한다. 
for i in range(2, N+1):
    if not i % 3 and not i%2:
        dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
    elif not i % 3:
        dp[i] = min(dp[i//3], dp[i-1]) + 1
    elif not i % 2:
        dp[i] = min(dp[i//2], dp[i-1]) + 1
    else:
        dp[i] = dp[i-1] + 1

print(dp[N])
