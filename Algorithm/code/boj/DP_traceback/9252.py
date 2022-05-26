"""
    LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
    모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

    예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
    첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.

"""
# LCS 2
from pprint import pprint

a = input()
b = input()
N, M = len(a), len(b)
dp = [[0]*(M+1) for _ in range(N+1)]

# dp[i][j] 는 a[:i] 와 b[:j] 를 비교했을 때 공통 문자열의 길이이다. 
for i in range(1, N+1):
    for j in range(1, M+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1 # 문자가 서로 같으면 대각선 위에서 1 더해서 내려온다.
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# pprint(dp)
# 아래와 같이 dp 배열이 채워진다. => 9251.py 
#   0 A C A Y K P
# 0 0 0 0 0 0 0 0
# C 0 0 1 1 1 1 1
# A 0 1 1 2 2 2 2
# P 0 1 1 2 2 2 3
# C 0 1 2 2 2 2 3
# A 0 1 2 3 3 3 3
# K 0 1 2 3 3 4 4

print(dp[N][M])
# Now traceback
# 오른쪽 아래에서 위로 올라오면서, 지나왔던 경로를 찾는다. 
if dp[N][M] != 0:
    i, j = N, M
    answer = ''
    cnt = 0
    while cnt < dp[N][M]:
        if a[i-1] == b[j-1]: # 만약 두 문자가 같다면, 대각선 왼쪽 위로 이동 (왔던 길로..)
            answer += a[i-1]
            cnt += 1
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i-1][j]: # 만약 두 문자가 다르다면, 왼쪽 혹은 위 중에서, 현재 dp[i][j] 값과 같은 곳으로 이동 
                i -= 1
            else:
                j -= 1
    print(answer[::-1]) 


