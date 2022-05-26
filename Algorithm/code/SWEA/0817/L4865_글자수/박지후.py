import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    pattern = input()
    target = input()

    count_dict = {k:0 for k in pattern}

    for c in target:
        if c in pattern:
            count_dict[c] += 1
    
    result = max(count_dict.values())

    print(f'#{tc} {result}')