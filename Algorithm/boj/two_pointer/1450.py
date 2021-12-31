"""
    세준이는 N개의 물건을 가지고 있고, 최대 C만큼의 무게를 넣을 수 있는 가방을 하나 가지고 있다.

    N개의 물건을 가방에 넣는 방법의 수를 구하는 프로그램을 작성하시오.
"""
# 방법의 수 !
# meet in the middle :
# 완전탐색의 경우 시간 복잡도가 O(2^N) 인 것을 반으로 쪼개어 시간 복잡도를 O(2^(n/2)) 로 줄인다. 

# 그룹을 A, B 2개로 나눈 뒤, 
# 완전탐색을 통해 각 그룹에서 가능한 모든 부분 집합과, 그 부분 집합의 합 A_sum 을 구한다.
# A_sum 을 하나 선택하여, C - A_sum 보다 작은 B_sum 을 찾는다. (이분 탐색 이용하여 찾음)
#                       이 때, 가방의 최대 무게 조건을 만족한다. 
# 조건을 만족한 B_sum 의 개수를 카운트한다. 

# 부분집합은 재귀적으로 찾는다. 
import bisect

def subset(i, size, w, items, sum_list):
    if i >= size:
        sum_list.append(w)
        return 

    subset(i+1, size, w, items, sum_list) # 부분집합에 미포함
    subset(i+1, size, w + items[i], items, sum_list) # 부분집합에 포함

N, C = map(int, input().split())
items = list(map(int, input().split()))

A, B = items[:N//2], items[N//2:] # 반으로 나눈다. 
A_sum_list, B_sum_list = [], [] 
subset(0, len(A), 0, A, A_sum_list) # A 의 모든 부분집합 각각의 합을 A_sum_list 에 저장 
subset(0, len(B), 0, B, B_sum_list)

B_sum_list.sort() # sort for binary search 
answer = 0 
for A_sum in A_sum_list:
    if C - A_sum >= 0: 
        # A_sum + B_sum <= C 를 만족하는 모든 B_sum 을 찾는다. 
        answer += bisect.bisect_right(B_sum_list, C - A_sum) # bisect_right 써야함. 0 인 경우도 포함해야 하므로.

print(answer)