N = int(input())

result_cnt = 0
result = []

for i in range(N//2, N+1):
    temp_cnt = 0 
    temp = [N, i]
    while temp[-2] - temp[-1] >= 0:
        temp.append(temp[-2] - temp[-1])
        temp_cnt += 1
    if temp_cnt > result_cnt:
        result_cnt = temp_cnt
        result = temp

print(result_cnt+2)
print(*result)