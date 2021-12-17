"""
    이 도시에는 두 대의 경찰차가 있으며 두 차를 경찰차1과 경찰차2로 부른다.
    처음에는 항상 경찰차1은 (1, 1)의 위치에 있고 경찰차2는 (N, N)의 위치에 있다. 
    경찰 본부에서는 처리할 사건이 있으면 그 사건이 발생된 위치를 두 대의 경찰차 중 하나에 알려 주고,
    연락 받은 경찰차는 그 위치로 가장 빠른 길을 통해 이동하여 사건을 처리한다. 
    (하나의 사건은 한 대의 경찰차가 처리한다.) 
    그리고 사건을 처리 한 경찰차는 경찰 본부로부터 다음 연락이 올 때까지 처리한 사건이 발생한 위치에서 기다린다. 
    경찰 본부에서는 사건이 발생한 순서대로 두 대의 경찰차에 맡기려고 한다. 
    처리해야 될 사건들은 항상 교차로에서 발생하며 경찰 본부에서는 이러한 사건들을 나누어 두 대의 경찰차에 맡기되, 
    두 대의 경찰차들이 이동하는 거리의 합을 최소화 하도록 사건을 맡기려고 한다.

    첫째 줄에 두 경찰차가 이동한 총 거리를 출력한다. 
    둘째 줄부터 시작하여 (i+1)번째 줄에 i(1 ≤ i ≤ W)번째 사건이 맡겨진 경찰차 번호 1 또는 2를 출력한다.
"""
from collections import deque

N = int(input())
W = int(input())
event = deque()
for _ in range(W):
    i, j = map(int, input().split())
    event.append((i-1, j-1))

# dp 를 생각해보자
# 두 경찰차가 이동한 거리가 최소가 되어야 한다.
# 비슷한 문제가 있을까..?

# event 1, 2, 3, 4, ... 
# 1. event 를 이분할 해서 cop 에 할당 한뒤 최단 거리를 찾는다 => 완전탐색
# 2. or 마찬가지로 dfs 로 하나의 이벤트를 cop1 or 2 에게 할당하는 경우 모두 탐색 

# 3. dp 로 구해보자 
# dp[i][0] => i 번째 사건을 cop 1 이 맡았을 때 최단거리 
# dp[i][1] => i 번째 사건을 cop 2 이 맡았을 때 최단거리 
# dp[i][0] = min(dp[i-1][0] + d0, dp[i-1][1] + d0) => d0 이 또 다른다. => 기억하고 있어야 함 
# dp[i][1] = min(dp[i-1][0] + d1, dp[i-1][1] + d1)
# i-1 까지의 최단거리가 i 까지의 최단거리를 보장하는가? 잘모르겠다.

# 4. https://ioqoo.tistory.com/41
# dp[i][j] = cop1 이 i, cop2 가 j 번째 사건까지 해결한 상태일 때, 앞으로의 이동거리 중 최솟값 

