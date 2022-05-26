
N, K = map(int, input().split())
temps = list(map(int, input().split()))

dp = []
dp.append(sum(temps[:K]))

answer = dp[0] 
start = 0
end = K
while end < N:
    now_sum = dp[-1] - temps[start] + temps[end]
    dp.append(now_sum)
    if now_sum > answer:
        answer = now_sum
    
    start += 1
    end += 1

print(answer)
