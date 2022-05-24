import sys
sys.stdin = open('input.txt')


def backtrack(cnt_c, now, N):
    global min_c

    if now >= N-1: # 현재 위치가 마지막 정류장 혹은 그 너머의 위치에 있는 경우 
        min_c = min(min_c, cnt_c-1) # 교환횟수의 최솟값 업데이트 
        return # 빠져나온다. 

    # 가지치기
    if cnt_c > min_c: # 이미 최솟값보다 더 많이 교환한 경우 
        return # 더 해볼 필요 없이 빠져나온다. 
    
    for nxt in range(now+1, now + Battery[now] + 1): # 현재 위치에서 남은 배터리로 갈 수 있는 곳 모두를 탐색한다. 
        backtrack(cnt_c+1, nxt, N) # 그 위치로 이동하여 배터리를 교환한다. 

T = int(input())
for tc in range(1, T+1):
    N, *Battery = map(int, input().split())
    Battery.extend([0]*100) # 잔여 배터리에 따라 마지막 정류장 너머로도 갈 수 있어서, 더미를 이용.

    now = 0
    min_c = float('inf') # 큰 값으로 초기화. 
    backtrack(0, now, N)

    print(f'#{tc} {min_c}')