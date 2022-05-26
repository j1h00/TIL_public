"""
    준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

    동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
"""
import sys

N, K = map(int, input().split())

coins = []
max_price = 0 
for i in range(N):
    coins.append(int(input()))
    if coins[i] <= K: # 만약 동전의 크기가 K 보다 작다면
        max_price = i # K 보다 작은 동전 중에, 가장 큰 동전을 업데이트 

cnt = 0 
while K: # K 가 0 보다 큰 경우 계속함. 
    cnt += K // coins[i] # cnt 는 필요한 동전의 개수  
    K %= coins[i] # K 를 나머지로 업데이트 
    i -= 1 # 다음 동전에 대해서 같은 작업을 한다. 

print(cnt)


