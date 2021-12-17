import sys

def rotate(board):
    N = len(board)
    new_board = []
    for c in range(N):
        temp = ""
        for r in range(N - 1, -1, -1):
            temp += board[r][c]
        new_board.append(temp)

    return new_board

def main():
    sys.stdin = open('input.txt')

    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        board = []
        for _ in range(N):
            board.append(input().split())

        print(f'#{tc}')

        one = rotate(board)
        two = rotate(one)
        thr = rotate(two)
        for i in range(N):
            print(one[i] + " " + two[i] + " " + thr[i])

main()

