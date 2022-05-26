import sys
sys.stdin = open('input.txt')


def check(now):
    x, y = now[0], now[1]
    for dx, dy in d:
        nx = x + dx
        ny = y + dy 
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == arr[x][y] + 1:
            dp[arr[x][y]] = 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    dp = [0] * (N**2 + 1) # 주변에 1 큰 수가 있는 지 표시할 dp 배열
    for i in range(N):
        for j in range(N):
            check([i,j]) # 사방을 확인하면서, 지금보다 1 큰 수가 있으면 dp 에 표시 
    
    answer = 0
    answer_start = 0
    i = 1
    while i <= N**2: # dp 배열의 앞에서부터 읽으면서 
        if dp[i]: # 1을 만나면 
            j = i
            cnt = 0 # i 부터 뒤에 1이 몇개 이어지는 지 j 인덱스로 확인한다. 
            while j <= N**2 and dp[j]:
                cnt += 1
                j += 1
            if cnt > answer: # 만약 1의 개수가 현재 최고 개수 보다 많다면 업데이트 
                answer = cnt
                answer_start = i 
            i += cnt 
        else: # 0 을 만나면 지나간다. 
            i += 1
                
    print(f'#{tc} {answer_start} {answer + 1}')
    