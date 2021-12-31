# 가장 긴 증가하는 부분 수열 3
# 12015 가장 긴 증가하는 부분 수열 2 와 입력 범위가 다르다. 
# 동일한 이분탐색 방법으로 성공.
import sys
import bisect

N = int(sys.stdin.readline())
A = [int(_) for _ in sys.stdin.readline().split()]


dp = [A[0]] # 가장 긴 증가하는 부분 수열을 저장할 dp 

for i in range(N):
    if A[i] > dp[-1]: # A[i] 가 증가하는 부분 수열을 만족시킨다면
        dp.append(A[i]) # 넣는다. 
    else: # 아니라면 
        idx = bisect.bisect_left(dp, A[i]) # dp 에 A[i] 를 삽입할 때, A[i] 가 삽입될 가장 왼쪽 인덱스를 반환함
        dp[idx] = A[i] # dp[idx] 를 A[i] 로 교체한다. 
        # 이를 통해 생성된 dp 리스트는 LIS 를 만족하지 않을 수 있지만, 가장 긴 길이를 구하는 데에는 문제가 없다.
        # (LIS 를 만족하지 않지만 교체 하는 이유는, 그 이후에 A[i] 를 잇는 최적의 수가 나와 LIS 를 생성할 수도 있기 때문임. ) 

print(len(dp))