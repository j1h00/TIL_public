import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    ticket = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    
    # 세번째 달까지 손수 초기화합니다.
    dp = [0] * 12
    dp[0] = min(plan[0]*ticket[0], ticket[1])
    dp[1] = dp[0] + min(plan[1]*ticket[0], ticket[1])
    dp[2] = min(ticket[2], dp[1] + plan[2]*ticket[0], dp[1] + ticket[1])
        
    for i in range(3, 12):
        dp[i] = min(dp[i-3] + ticket[2], dp[i-1] + plan[i]*ticket[0], dp[i-1] + ticket[1])
    
    answer = min(dp[11], ticket[3])
    print(f'#{tc} {answer}')