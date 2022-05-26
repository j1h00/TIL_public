"""
    세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다. 
    이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.

    배열 A와 B의 인덱스는 1부터 시작한다.
"""

# ex) N = 3 
# 1행 => 1 2 3 
# 2행 => 2 4 6 구구단 2단
# 3행 => 3 6 9 구구단 3단
import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())



left = 1
right = N*N

while left <= right:
    mid = (left + right) //2 # mid 는 1 ~ N^2 범위의 모든 수 가운데, 중앙에 위치한 수다. 

    # mid 의 일차원 배열에서의 위치를 찾은 뒤에, 그 위치를 k 와 비교한다. 
    mid_index = 0 # 1차원 배열로 옮겼을때, mid 의 인덱스를 뜻한다. 
    for i in range(1, N+1): # i 는 행 번호 
        mid_index += min(mid // i, N) # 각 행마다, mid 보다 작거나 같은 수의 개수를 구한다. 

    if mid_index >= k: # 만약 mid_index가 k 보다 크다면, 왼쪽 절반을 택한다. 
        right = mid - 1
    else: # 아니라면, 오른쪽 절반을 택한다. 
        left = mid + 1

print(left)