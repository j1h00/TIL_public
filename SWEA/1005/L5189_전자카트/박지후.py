import sys
sys.stdin = open('input.txt')


# 재귀를 이용한 백트래킹 방식으로 경로 탐색
# 배터리 최소 사용량을 이용해 가지치기 
def dfs(battery, stack, N):
    global MIN_battery

    if len(stack) == N: 
        # 경로 끝에 도달했다면, 경로 끝에서 사무실로 돌아가는 비용까지 더해 최소 비용 계산 
        MIN_battery = min(MIN_battery, battery +  graph[stack[-1]][0]) 
        return 

    if battery > MIN_battery: # 가지치기, 배터리 사용량이 이미 최소 사용량 보다 많으면 더 해볼 필요 없음
        return 

    promising = [] # 지금까지 가지 않은 곳을 저장하는 배열 
    for i in range(N):
        if i not in stack: # 갔던 곳은 제외하고 저장.
            promising.append(i)

    for p in promising: # 남아있는 곳에 대하여 다시 dfs 
        dfs(battery + graph[stack[-1]][p], stack + [p], N)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))

    MIN_battery = float('inf')
    stack = [0]
    dfs(0, stack, N)

    print(f'#{tc} {MIN_battery}')
    


