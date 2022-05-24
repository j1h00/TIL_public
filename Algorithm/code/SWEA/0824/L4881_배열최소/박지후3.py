import sys
sys.stdin = open('input.txt')


def backtrack(stack):
    if len(stack) == N:
        result.append(stack)
        return

    promising = list(range(N))
    for i in stack:
        if i in promising:
            promising.remove(i)

    if promising:
        for p in promising:
            stack.append(p)
            backtrack(stack[:])
            stack.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    result = []
    for i in range(N):
        stack = [i]
        backtrack(stack[:])

    answer = []
    MIN = 10**2
    for perm in result:
        temp_sum = 0
        for row, p in enumerate(perm):
            temp_sum += arr[row][p]
        if temp_sum < MIN:
            MIN = temp_sum

    print(f'#{tc} {MIN}')







    