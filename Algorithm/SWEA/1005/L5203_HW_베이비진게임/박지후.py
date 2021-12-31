import sys
sys.stdin = open('input.txt')


def is_baby_gin(cards): # baby gin 의 여부를 확인한다. 
    for i in range(len(cards)-2): # triplet 확인
        if cards.count(cards[i]) >= 3:
            return True

    cards = sorted(list(set(cards))) # 중복 제거 후 정렬
    for i in range(len(cards)-2): # run 확인
        if cards[i+1] == cards[i] + 1 and cards[i+2] == cards[i] + 2:
            return True

    return False 
    

T = int(input())
for tc in range(1, T+1):
    all_cards = list(map(int, input().split()))

    p1 = [all_cards[i] for i in range(0, 12, 2)] # 플레이어1 의 카드들
    p2 = [all_cards[i] for i in range(1, 12, 2)] # 플레이어2 의 카드들 

    winner = 0 # 승자는?
    for i in range(3, 6): # 베이비진을 확인하기 위해, 일단 카드 3장 부터 시작하여 한장씩 추가 
        if is_baby_gin(p1[:i+1]): # 플레이어 1이 현재까지 받은 카드들을 대상으로 baby gin 확인
            winner = 1
            break
        if is_baby_gin(p2[:i+1]): 
            winner = 2
            break

    print(f'#{tc} {winner}')