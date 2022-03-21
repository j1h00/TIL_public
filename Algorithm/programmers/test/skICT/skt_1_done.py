"""

1원 당 생산 단가가 가장 싼 환폐를 찾는다. 
"""

def solution(money, costs):
    coins = [1, 5, 10, 50, 100, 500]

    # 1원 당 생산 단가가 가장 싼 동전을 찾기 위해 비율을 계산하여 배열에 저장한다. 
    ratios = []
    for i in range(6):
        ratios.append((coins[i] / costs[i], coins[i], costs[i]))
    
    ratios.sort(reverse=True) # 비율 순서대로 정렬한다. 
    
    # 비율이 가장 높은 동전 순서대로 사용하여 money 를 채워간다. 
    total_cost = 0
    for ratio, coin, cost in ratios:
        num = money // coin 
        rest = money % coin 

        total_cost += num * cost
        money = rest
        if not money: # money 를 모두 채우면 그만 둔다.
            break 
    
    return total_cost


answer1 = solution(4578, [1, 4, 99, 35, 50, 1000])
answer2 = solution(1999, [2, 11, 20, 100, 200, 600])

print(answer1, answer2)

