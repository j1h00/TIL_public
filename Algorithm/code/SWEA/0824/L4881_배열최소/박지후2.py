import sys
import itertools
sys.stdin = open('input.txt')

def backtrack(arr, stack, visited, N, row):
    if row == N:
        result.append(sum(stack))
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                stack.append(arr[row][i])
                backtrack(arr, stack, visited, N, row+1)
                stack.pop()
                visited[i] = 0
                
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    stack = []
    result = []
    visited = [0]*N
    backtrack(arr, stack, visited, N, 0)
    print(f'#{tc} {min(result)}')



    