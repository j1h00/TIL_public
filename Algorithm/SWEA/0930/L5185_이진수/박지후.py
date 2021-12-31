import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, HEX = input().split()
    N = int(N)
    DEC = int(HEX, 16)
    BIN = bin(DEC)
    
    # print(HEX)
    # print(DEC)
    # print(BIN)

    answer = format(DEC, 'b')
    while len(answer) % 4:
        answer = '0' + answer
    print(f'#{tc} {answer}')
