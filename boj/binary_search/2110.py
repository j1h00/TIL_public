"""
    도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

    도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 
    최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 
    한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

    C개의 공유기를 N개의 집에 적당히 설치해서, "가장 인접한 두 공유기 사이의 거리를 최대로" 하는 프로그램을 작성하시오.
"""
import sys

N, C = map(int, sys.stdin.readline().split())
home = []
for i in range(N):
    home.append(int(sys.stdin.readline()[:-1]))

home = sorted(home)

def cnt_wifi(mid): # 두 공유기 사이의 최소 거리를 mid 로 지정했을 때, 놓을 수 있는 공유기의 개수   
    last_home = home[0]
    cnt = 1
    for now in home:
        if now - last_home >= mid: # 두 집 사이의 거리가 mid 보다 크다면 
            last_home = now # 
            cnt += 1
    return cnt
        
min_d = 1 # 인접한 두 공유기 사이의 최소 거리의 최소 최대 범위 
max_d = home[-1] - home[0] #   

while min_d <= max_d:
    mid = (min_d + max_d) // 2 
    if cnt_wifi(mid) >= C: # 최소 거리를 mid 로 지정했을 때, 놓을 수 있는 공유기의 개수가 C 보다 크다면 
        min_d = mid + 1 # 거리를 더 늘려도 된다. 
    else:
        max_d = mid - 1

print(max_d)
