# 2580 스도쿠 
import sys

def dfs(z): # z 는 zeroes 리스트의 인덱스를 뜻함.
    global flag

    if flag:
        return

    if z == len(zeroes): # 만약 모든 0 을 다 채웠다면 
        for i in range(9): 
            print(*sudoku[i]) # 채운 스도쿠 판을 출력 
        flag = True # 찾았음을 표시 
        return

    i, j = zeroes[z]

    possible = x_find_and_check(i, j) # i,j 에 가능한 수를 모두 찾는다. 
    if possible: # 가능한 수가 있다면 
        for x in possible: # 모든 x 에 대해 dfs 탐색을 한다. 
            sudoku[i][j] = x
            dfs(z + 1) 
            sudoku[i][j] = 0

def x_find_and_check(i, j):
    result = list(range(1, 10)) 

    for k in range(9): # 일단, 가로, 세로 줄을 모두 확인한다. 
        if sudoku[i][k] in result:
            result.remove(sudoku[i][k]) 
        if sudoku[k][j] in result:
            result.remove(sudoku[k][j])
    
    x = 3*(i//3)
    y = 3*(j//3)
    # 3x3 box 를 확인한다. 
    for r in range(x, x+3):
        for c in range(y, y+3):
            if sudoku[r][c] in result:
                result.remove(sudoku[r][c])

    return result


sudoku = []

for i in range(9):
    row = map(int, sys.stdin.readline().split())
    sudoku.append(list(row))

zeroes = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

flag = False
# 인덱스 0 부터, 0을 채워나가기 시작한다. 
dfs(0)

    
