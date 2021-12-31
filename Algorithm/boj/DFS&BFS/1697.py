"""
    수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
    수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
    순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

    수빈이와 동생의 위치가 주어졌을 때, 
    수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
"""
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

road = [0]*1000001

queue = deque()
queue.append(N)

flag = 0
while queue:
    now = queue.popleft()
    if now == K: # 동생을 만나면 break 
        print(road[now])
        break 
    moves = [now + 1, now - 1 , now * 2] # 이동할 수 있는 선택지 
    for move in moves:
        if 0 <= move <= 100000: # 범위 내에서 
            if road[move] == 0: # 한번도 오지 않았던 곳이라면 
                queue.append(move) 
                road[move] = road[now] + 1 # 몇 초 만에 도달했는지 표시 
