"""
    10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 
    이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 
    가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
"""
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
seq = list(map(int, input().split()))

seq_sum = [0] 
# 합을 미리 계산하여 둔다 (seq_sum[x] 는 seq[:x]의 합을 저장해 둔 값이다.)
# 따라서 seq_sum 의 마지막 인덱스는 N 이다. 
for i in range(1, N+1):
    seq_sum.append(seq[i-1] + seq_sum[i-1])

answer = N+1

l = 0 
r = 1 
while r < N+1:
    now_sum = seq_sum[r] - seq_sum[l] # now_sum 은 seq[l-1] 부터 seq[r-1] 까지 모두 더한 값이다. 
    if now_sum >= S: 
        answer = min(answer, r-l)
        l += 1
    else:
        r += 1

if answer == N+1:
    print(0)
else:
    print(answer)
        