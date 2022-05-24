# N-Queen 
import sys

N = int(sys.stdin.readline())

def check(i, row_col):
    # col check
    if i in row_col: # row_col 에 같은 열이 있는지 확인한다. 
        return False
    
    # diagonal check 
    now_r, now_c = len(row_col), i # 같은 대각선 상에 있는지 확인한다. 
    for r, c in enumerate(row_col):
        if abs(now_r - r) == abs(now_c-c): # 행끼리의 차 절댓값 == 열끼리의 차 절댓값 일 경우 같은 대각선 상에 있다.  
            return False
            
    return True 

def dfs(row_col, N):
    global cnt 

    if len(row_col) == N: # 퀸을 N 개 놓은 경우 
        cnt += 1 # 경우의 수 추가 
        return 
    
    for i in range(N): # i 는 열의 인덱스를 뜻함 
        if check(i, row_col): # check 해본다. (i 를 row_col 에 추가해도 되는지!)
            row_col.append(i)
            dfs(row_col, N)
            row_col.pop()

cnt = 0 # 경우의 수 
row_col = [] 
# ex) => row_col 의 인덱스 5 위치에 3 이 있다. => 6번 행에서는 3번 열을 선택함.

dfs(row_col, N)

print(cnt)
    
