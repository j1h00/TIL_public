import sys

def main():
    sys.stdin = open('input.txt')

    T = int(input())
    for tc in range(1, T+1):
        board = [[-1]*15 for _ in range(5)]

        for i in range(5):
            row = input()
            for j in range(len(row)):
                board[i][j] = row[j]

        answer = ""
        for j in range(15):
            for i in range(5):
                if board[i][j] != -1:
                    answer += board[i][j]

        print(f'#{tc} {answer}')

main()

