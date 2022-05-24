"""
45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.
"""
import sys

N = int(sys.stdin.readline())

dp = [[1]*10 for _ in range(N+1)] # 2차원 배열
# ex) => dp[5][4] 는 길이가 5이면서, 4로 끝나는 계단수를 뜻한다. 
dp[1][0] = 0 
for i in range(2, N+1):
    dp[i][0] = dp[i-1][1] # 길이가 i 면서, 0 으로 끝나는 계단수는 => 길이가 i-1 이고 1로 끝나는 계단수에 0 을 붙인 값밖에 없다. 
    dp[i][9] = dp[i-1][8]
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

answer = 0 
for i in range(10):
    answer += dp[N][i]

print(answer%(10**9))
