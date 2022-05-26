import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N, pw = input().split()

    stack = [0]
    for c in pw:
        if stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    print(f'#{tc} {"".join(stack[1:])}')

