import sys
from collections import deque # 오븐 회전에 사용했습니다. 
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))

    # N 개를 화덕에 넣고 시작. 
    oven = deque(range(N)) # oven 안에 있는 수는, pizzas 의 피자 번호를 뜻합니다. 
    ready_for_oven = N # 다음에 넣어야할 피자의 번호를 저장합니다. 

    while len(oven) > 1: # 개수가 1개가 되면 끝나도록 하였습니다. 
        now = oven.popleft() # 피자를 하나 빼서 
        pizzas[now] //= 2 # 해당하는 피자의 치즈 수를 // 2 만큼 줄입니다. 
        if pizzas[now]: # 만약 꺼냈던 피자의 치즈가 남았다면, 화덕에 다시 넣습니다. 
            oven.append(now)
        elif ready_for_oven < M: # 만약 꺼냈던 피자의 치즈가 남지 않았다면, 넣어야할 다른 피자가 남아있는 지 봅니다. 
            oven.append(ready_for_oven) # 남은 피자를 하나 오븐에 넣습니다. 
            ready_for_oven += 1 # 다음에 넣어야할 피자의 번호를 갱신합니다. 
    
    print(f'#{tc} {oven.pop() + 1}') 
            

