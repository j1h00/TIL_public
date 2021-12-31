import sys
from collections import deque
sys.stdin = open('input.txt')

def cycle(data: deque):
    cnt = 1  
    while data[-1]:
        now = data.popleft() - cnt
        if now < 0:
            data.append(0)
            break 
        else:
            data.append(now)
        cnt = cnt % 5 + 1 
    return data

def step_down(data):
    MIN = min(data)
    step = (MIN//15 - 1) * 15
    for i in range(len(data)):
        data[i] -= step 
    return data
        
T = 10
for tc in range(1, T+1):
    tc = int(input())
    data = list(map(int, input().split()))

    min_data = step_down(data)

    result = list(cycle(deque(min_data)))

    print(f'#{tc}', end = " ")
    print(*result)