import sys
sys.stdin = open("input.txt")

def find_palindrome(board, N):
    length = 1 
    for M in range(N, length, -1):              # 회문의 길이가 가장 큰 것부터 찾습니다. 
        for row in board:
            for start in range(N-M+1):
                end = start + M - 1
                if row[start] == row[end]:
                    if is_palindrome(row, start+1, end-1):
                        length = max(length, end - start + 1)
                        return length           # 찾으면, 현재 회문의 길이를 리턴합니다. 

    return length                               # 찾지 못하면, 가장 긴 회문의 길이는 1입니다. 

def is_palindrome(row, start, end):
    while start < end:
        if row[start] != row[end]:
            return False
        else:
            start += 1
            end -= 1
    return True 


T = 10

for tc in range(1, T+1):
    tc = int(input())
    N = 100

    board = []
    for i in range(N):
        board.append(input())
    result1 = find_palindrome(board, N)
    result2 = find_palindrome(list(zip(*board)), N)
 
    print(f'#{tc} {max(result1, result2)}')