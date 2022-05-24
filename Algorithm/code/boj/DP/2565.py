"""
    전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서부터 차례대로 번호가 매겨진다. 
    전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때,
    남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하는 프로그램을 작성하시오.
"""
import sys

N = int(sys.stdin.readline())
dp = [1]*N
A = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    A.append((a,b))

# a (왼쪽 전봇대) 에 대해서 정렬한다. 
A.sort(key = lambda x : x[0])

# b (오른쪽 전봇대) 에 대해서, 가장 긴 증가하는 부분 수열을 구한다. 
for i in range(1, N):
    for j in range(i):
        if A[i][1] > A[j][1] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1
    
print(N - max(dp))