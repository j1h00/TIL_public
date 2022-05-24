import sys
sys.stdin = open('input.txt')

# 아래 블로그와 동일하게 보이어-무어 알고리즘을 따라 치며 연습해보았습니다.
# https://mungto.tistory.com/124
def boyermoore(pattern, target):
    p = len(pattern)
    t = len(target)

    i = 0 
    while i <= t-p:
        # 마지막 글자부터 비교 
        j = p-1 
        while j >= 0:
            if pattern[j] != target[i + j]:
                # 뛰어넘을 만큼을 계산 (target 의 마지막과 같은 글자가 pattern 에 있는지 찾아서 점프)
                move = find(pattern, target[i+p-1])
                break
            j -= 1
        if j < 0:
            return 1 
        else:
            i += move
    return 0 

def find(pattern, c):
    for i in range(len(pattern)-2, -1, -1):
        if pattern[i] == c:
            return len(pattern) -i -1
    return len(pattern)

T = int(input())

for tc in range(1, T+1):
    pattern = input()
    target = input()

    # result = 0
    # if pattern in target:
    #     result = 1 
    result = boyermoore(pattern, target)

    print(f'#{tc} {result}')