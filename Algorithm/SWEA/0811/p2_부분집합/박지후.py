import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(T):
    num_list = list(map(int, input().split()))
    n = len(num_list)

    result = 0 
    for i in range(1<<n):	
        subset_sum = 0
        for j in range(n): 
            if i & (1<<j):
                subset_sum += num_list[j]
        if subset_sum == 0:
            result = 1 

    print(f'#{tc} {result}')