import sys
sys.stdin = open('input.txt')


def make_decimal_candidates(num, n): 
    candidates = []

    for i in range(len(num)): # num 의 모든 자리를 한번씩 확인하면서,
        for k in range(1, n): # 그 자리를, 다른 n 진수 숫자로 변경하기 위한 k, 
            changed = str((int(num[i]) + k) % n) # 다른 n 진수 숫자로 변경한다. 
            tmp = num[:i] + changed + num[i+1:] # tmp 에 변경한 str 을 저장
            candidates.append(to_decimal(str(int(tmp)), n)) # 변경된 tmp 를 10진수로 바꾸어 candidate 에 저장

    return candidates

def to_decimal(num, n): # 10 진수 수로 변경한다. 
    result = 0
    cnt = 0
    for d in num[::-1]:
        result += int(d) * (n ** cnt)
        cnt += 1

    return result

T = int(input())
for tc in range(1, T+1):
    bi = input()
    tr = input()

    bi_candidates = make_decimal_candidates(bi, 2) # 2진수 후보
    tr_candidates = make_decimal_candidates(tr, 3) # 3진수 후보
    answer = list(set(bi_candidates) & set(tr_candidates)) # 겹치는 것을 찾는다. 
 
    print(f'#{tc} {answer[0]}')
    