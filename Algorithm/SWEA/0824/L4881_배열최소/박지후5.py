import sys

sys.stdin = open('input.txt')

# 현재 row 에서 가능한 column index 를 찾아서, stack 에 원소를 추가합니다.
def backtrack(visited, stack, row, N):
    global MIN 

    # stack 에 N 개의 원소가 있다면,
    if len(stack) == N:
        if sum(stack) < MIN:
            MIN = sum(stack) # 최솟값을 업데이트
        return

    # 가지치기!!
    if sum(stack) >= MIN:
        return 

    # 방문하지 않은 column 이면, 좌표에 해당하는 배열 원소를 stack 에 추가하고, visited 에 방문 표시 합니다.
    for i in range(N):
        if not visited[i]:
            stack.append(arr[row][i])
            visited[i] = 1
            backtrack(visited, stack, row + 1, N)
            stack.pop() # 윗 줄에서 backtrack() 함수가, 현재 가능한 경우를 모두 탐색하고 나오면
            visited[i] = 0 # stack 과 visited 의 기록을 지웁니다.

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    MIN = 10*10 # 초기에 최댓값으로 설정
    visited = [0]*N
    stack = []
    backtrack(visited, stack, 0, N) # 방문기록, stack, 현재 행, N

    print(f'#{tc} {MIN}')







