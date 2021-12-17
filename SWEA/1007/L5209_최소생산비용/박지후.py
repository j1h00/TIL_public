import sys
sys.stdin = open('input.txt')


def backtrack(p_idx, stack, cost, N):
    global min_cost

    if p_idx == N: # 마지막 제품까지 공장을 지정한 경우 (함수 설계 상 N-1 이 아니라, N 이다.)
        min_cost = min(min_cost, cost) # 최소 생산 비용 업데이트 
        return # 빠져나온다. 

    if cost > min_cost: # 이미 비용이 최소 생산 비용을 뛰어 넘은 경우 
        return # 더 해볼 필요 없이 빠져나온다. 

    factory_left = [] # 아직 지정되지 않은 공장을 확인한다. 
    for i in range(N):
        if i not in stack:
            factory_left.append(i)

    for f in factory_left: # 현재 제품인 p_idx 에 공장을 할당하고 (stack + [f]), 다음 제품을 확인하러 간다. 
        backtrack(p_idx + 1, stack + [f], cost + arr[p_idx][f], N)
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    min_cost = float('inf') # 최소값을 구하기 위해 큰 값으로 초기화 
    backtrack(0, [], 0, N)

    print(f'#{tc} {min_cost}')