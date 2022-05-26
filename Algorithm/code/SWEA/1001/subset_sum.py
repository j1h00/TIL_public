# arr 부분집합의 합이 0이되는 경우의 수
arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)

# 1. itertools
from itertools import combinations

cnt = 0
for n in range(N+1):
    # n == 부분집합 원소의 개수
    subsets = combinations(arr, n)
    for subset in subsets:
        if sum(subset) == 0:
            cnt += 1
print(cnt)


# 2. << bitwise operator
cnt = 0
# number of cases => 모든 경우의 수
noc = 1 << N
for i in range(noc):
    sum_of_subset = 0
    for j in range(N):
        if i & (1 << j):
            sum_of_subset += arr[j]
    if sum_of_subset == 0:
        cnt += 1
print(cnt)


# 3. 재귀(완전탐색)
subset = []
total = 0


def comb(idx):
    global total

    if idx == len(arr):
        if sum(subset) == 0:
            total += 1
        return

    subset.append(arr[idx])
    comb(idx+1)

    subset.pop()
    comb(idx+1)


comb(0)
print(total)

