def dfs(board):
    global cnt

    now1 = sum(board[0])
    now2 = sum(board[1])
    if now1 == N and now2 == N:
        cnt += 1
        return
    if N-now1 >= 2:
        add_block1()
        dfs(board)
        back()
        add_block2()
        dfs(board)
        back()
        add_block3()
        dfs(board)
        back()

    else:
        add_block1()
        dfs(board)
        back()



def add_block1():
    board[0].append(1)
    board[1].append(1)

def add_block2():
    board[0].append(2)
    board[1].append(2)

def add_block3():
    board[0].append(2)
    board[1].append(2)

def back():
    board[0].pop()
    board[1].pop()


T = int(input())

for tc in range(1, T+1):
    N = int(input()) // 10


    board = [[],[]]
    cnt = 0
    dfs(board)

    print(f'#{tc} {cnt}')
