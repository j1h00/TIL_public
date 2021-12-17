import sys
sys.stdin = open('input.txt')


def dfs(item_idx, cnt): # 배열에 item 을 하나씩 담아서 조합을 만든다고 생각하고 dfs 정의 
    global MIN_diff

    if cnt == N//2: # 담은 item 이 N//2 개가 되었을 때, 
        stack = []
        stack2 = []
        
        for i in range(N):
            if visited[i]: # 선택한 item 을 stack 에 저장 
                stack.append(i)
            else: # 선택하지 않은 item 을 stack2 에 저장
                stack2.append(i)

        total1 = 0 # 선택한 item 들의 시너지 계산 
        for i in stack:
            for j in stack:
                total1 += S[i][j] 

        total2 = 0 # 선택하지 않은 item 들의 시너지 계산 
        for i in stack2:
            for j in stack2:
                total2 += S[i][j] 

        MIN_diff = min(MIN_diff, abs(total1-total2)) # 최솟값 업데이트 
        return

    for item in range(item_idx, N): # 직전에 선택한 item 은 선택하지 않도록, item_idx ~ N 까지만 item 확인 
        if not visited[item]: # 선택하지 않은 item 이라면 
            visited[item] = 1
            dfs(item + 1, cnt + 1) # 선택한 item 이후의 item 만 선택하도록 item + 1, 선택한 갯수 + 1 
            visited[item] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    S = []
    for _ in range(N):
        S.append(list(map(int, input().split())))

    visited = [0] * N     
    MIN_diff = float('inf') 
    dfs(0, 0)

    print(f'#{tc} {MIN_diff}')