"""
양팔 저울과 몇 개의 추가 주어졌을 때, 
이를 이용하여 입력으로 주어진 구슬의 무게를 확인할 수 있는지를 결정하려고 한다.
"""
# dfs 재귀적 풀이를 이용한다. 
# i 번째 무게추를 
# 1. 왼쪽에 올린다. 
# 2. 오른쪽에 올린다.
# 3. 사용하지 않는다.  
# 3가지 경우를 모두 탐색하여, 특정한 무게를 만들 수 있는 지 여부를 2차원 DP 배열에 저장한다. 
# 대신 모든 경우에 대해 재귀적으로 실행할 시에 3**i 번 실행해야 하므로 
# 가지치기가 필요하다. => 중복된 상황을 다시 가지 않는다. ( https://source-sc.tistory.com/3 의 예제에서 잘 설명해주고 있다.)
# ex) 5번까지의 추를 이용하여 왼쪽과 오른쪽 무게의 차이가 2인 경우를 만들었다고 하자, 
# 그러나 왼쪽과 오른쪽 무게의 차이가 똑같이 2 이지만, 사용한 추의 조합이 다른 경우가 존재한다. 
# => 이 경우 굳이 또, 6번째 추에 대해 탐색할 필요가 없다 (중복된다)

# 재귀적 풀이와, 단순 DP 를 사용한 풀이 2개가 존재하는 듯 하다.  
N = int(input())
chu = list(map(int, input().split()))

K = int(input())
biz = list(map(int, input().split()))

LIMIT = 40000
dp = [0]*(LIMIT + 1) # index 무게를 만들 수 있는가 boolean 여부 
dp[0] = 1

for i in range(N): # 현재 추의 인덱스 
    tmp = dp[:]
    for w in range(LIMIT):
        if dp[w]: # 이미 만들 수 있는 무게에 대해서만
            tmp[w] = 1 # w 를 만들 수 있고, 
            tmp[w + chu[i]] = 1 # w + chu[i] 도 만들 수 있고 
            if chu[i] - w >= 0: # 현재 무게에서, 추의 무게를 뺀 값도 만들 수 있다. 
                tmp[chu[i] - w] = 1
            else:
                tmp[w - chu[i]] = 1
    dp = tmp[:]

for b in biz:
    if dp[b]:
        print('Y', end = " ")
    else:
        print('N', end = " ")
        