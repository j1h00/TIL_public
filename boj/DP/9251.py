"""
    LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 
    모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

    예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
"""
import sys

seq1 = sys.stdin.readline()[:-1]
seq2 = sys.stdin.readline()[:-1]


N = len(seq1)
M = len(seq2)

table = [[0]*(M+1) for _ in range(N+1)] # 2차원 배열 DP 이용  

# DNA sequence comparison 과 유사함. 
for i in range(1, N+1):
    for j in range(1, M+1):
        if seq1[i-1] == seq2[j-1]: # seq1 의 i 번째와, seq2 의 j 번째 문자가 같은 경우 
            table[i][j] = table[i-1][j-1] + 1 # 대각선 왼쪽 위에서 1 더해서 내려온다. 
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1]) 

print(table[N][M])