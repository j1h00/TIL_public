import sys
sys.stdin = open("input-long.txt")

def is_palindrome(row, start, end):
    while start < end:
        if row[start] != row[end]:
            return False
        else:
            start += 1
            end -= 1
    return True 


T = int(input())

for tc in range(1, T+1):
    seq = input()
    result = is_palindrome(seq, 0, len(seq)-1)

    print(f'#{tc} {result}')