import sys
from collections import deque

def main():
    sys.stdin = open('input.txt')

    T = int(input())
    for tc in range(1, T+1):
        days = int(input())
        price = deque(map(int, input().split()))

        buy_cnt = 0 
        profit = 0

        price.append(0)
        sell_price = max(price)

        for i in range(days):
            now_price = price.popleft()
            # print(price, sell_price, now_price, buy_cnt, profit)
            if now_price == sell_price:
                profit += sell_price * buy_cnt
                buy_cnt = 0
                sell_price = max(price)
            elif now_price < sell_price:
                buy_cnt += 1
                profit -= now_price

        print(f'#{tc} {profit}')

main()

