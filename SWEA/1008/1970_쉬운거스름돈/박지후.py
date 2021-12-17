import sys
sys.stdin = open('input.txt')
    

T = int(input())
for tc in range(1, T+1):
    total = int(input())

    coin = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    answer = [0] * len(coin)
    cnt = 0
    for i in range(len(coin)):
        now_coin = coin[i]
        if total >= now_coin:
            answer[i] = total // now_coin
            total -= now_coin * (answer[i]) 


    print(f'#{tc}')
    print(*answer)