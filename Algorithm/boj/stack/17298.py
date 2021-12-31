"""
    크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. 
    Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

    예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. 
    A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.
"""

import sys

N = int(sys.stdin.readline()[:-1])
A_list = list(map(int, sys.stdin.readline().split()))


# 2중 for문 사용 시 시간초과!!
# stack 사용!
answer = [-1] * N 
stack = [0]
for i in range(1, N):
    while stack and A_list[stack[-1]] < A_list[i]: # ex) => 처음엔 A[0] vs A[1] 
        answer[stack.pop()] = A_list[i] # A[1] 이 더 크다면 answer[0] 을 A[1] 로 업데이트 (NGE(0) = A[1])
    stack.append(i) # 오큰수를 구하지 못하였더라도, stack 에 추가해야함. => while 문을 돌면서 stack 에 있는 모든 수를 비교 

print(*answer)
