"""
    하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다. 
    하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다. 
    7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다. 
    또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.

    자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.
"""

# 시간초과 => 에라토스테네스의 채를 이용해라!!!
# def is_prime(N):
#     for i in range(2, N//2 + 1):
#         if not (N % i):
#             return False
#     return True 

N = int(input())

prime_bool = [True] * (N+1)

# 에라토스테네스의 채 
for i in range(2, int(N+1 ** 0.5)):
    if prime_bool[i]:
        for j in range(i+i, N+1, i): # i 보다 큰 수 중에 i 의 배수는 모두 제거한다. 
            prime_bool[j] = False 
prime_nums = [i for i, j in enumerate(prime_bool) if j == True and i >=2 ]

#0~i까지의 부분합 리스트를 만들어줌
prime_sums = [0] * (len(prime_nums) + 1)
for i in range(len(prime_nums)):
    prime_sums[i+1] = prime_sums[i] + prime_nums[i] 

l = 0
r = 1
cnt = 0
X = len(prime_nums)
while r < X+1:
    now_sum = prime_sums[r] - prime_sums[l]
    if now_sum == N:
        cnt += 1
        l += 1
    elif now_sum < N:
        r += 1
    else:
        l += 1

print(cnt)
        


