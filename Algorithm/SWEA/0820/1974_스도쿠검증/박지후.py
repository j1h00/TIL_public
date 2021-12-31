import sys

def is_sudoku(board):
    for row in board:
        if len(set(row)) != 9:
            return 0

    for col in zip(*board):
        if len(set(col)) != 9:
            return 0

    for j in range(3):
        box = []
        for i in range(3):
            row = board[i][j*3:j*3 + 3]
            box.extend(row)
        if len(set(box)) != 9:
            return 0

    return 1

def main():
    sys.stdin = open('input.txt')

    T = int(input())
    for tc in range(1, T+1):
        board = []
        for _ in range(9):
            board.append(input().split())

        print(f'#{tc} {is_sudoku(board)}')

main()

