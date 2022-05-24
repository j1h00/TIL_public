import sys

def main():
    sys.stdin = open('input.txt')

    T = int(input())
    for tc in range(1, T+1):

        board = [0]*200
        N = int(input())

        for _ in range(N):
            start, end = map(int, input().split())
            if start > end:
                start, end = end, start
            start = (start-1) // 2
            end = (end-1) // 2
            for i in range(start, end+1):
                board[i] += 1

        print(f'#{tc} {max(board)}')

main()

