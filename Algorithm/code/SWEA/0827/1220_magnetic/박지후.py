import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    cnt = 0 # 교착 상태 갯수를 저장합니다. 
    for j in range(N):
        ceiling = False # 위쪽이 천장으로 막혀있는지.. 즉 N 극 자성체의 유무를 저장합니다. 
        for i in range(N): # 행을 하나씩 이동하면서 탐색합니다. 
            if arr[i][j] == 1: # 만약 N 극을 만나면, 
                ceiling = True # 이 아래에 있는 S 극은 위로 빠져나갈 수 없으므로 천장이 막혀있음을 표시합니다. 
            if ceiling and arr[i][j] == 2: # 만약 위에 N 극이 있는 상태에서, S 극을 만난다면 교착 상태 조건을 충족합니다. 
                cnt += 1 # 교착 상태 갯수를 하나 올립니다. 
                ceiling = False # 다른 교착 상태를 찾기 위해 초기화합니다. 

    print(f'#{tc} {cnt}')
            