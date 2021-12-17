"""
    n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 
    이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 
    그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

    사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.
    시간 제한	메모리 제한	
      0.5 초 	 4 MB
"""

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0]*(k+1) # dp[x] : x 원을 만들 수 있는 경우의 수 
dp[0] = 1 # dp[3-3] = 1 을 만들기 위해 

for c in coins: 
    for i in range(c, k+1): 
        dp[i] += dp[i-c] 
        # ex) c = 3, i = 5 일때, 기존의 dp[5] 에, dp[5-3] 의 경우의 수를 더해준다 
        

print(dp[k])