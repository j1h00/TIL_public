import sys
sys.stdin = open("input.txt")

def find_palindrome(board, N, M):
    for row in board:
        for start in range(N-M+1):
            end = start + M - 1
            if row[start] == row[end]:                      # 처음과 끝 글자가 같다면
                if is_palindrome(row, start+1, end-1):      # 회문인지 확인합니다. 
                    return row[start: end+1]                

def is_palindrome(row, start, end):
    while start < end:                  
        if row[start] != row[end]:      # 처음과 끝 글자를 서로 비교하며,
            return False                # 만약 다르다면 회문이 아닙니다. 
        else:
            start += 1                  # 처음 위치와 끝 위치를 한칸씩 이동시킵니다. 
            end -= 1
    return True 


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    board = []
    for i in range(N):
        board.append(input())
    
    result1 = find_palindrome(board, N, M)

    if result1:
        print(f'#{tc} {result1}')
    else:
        result2 = find_palindrome(list(zip(*board)), N, M)
        print(f'#{tc} {"".join(result2)}')