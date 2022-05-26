import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    text = input()
    ok = True
    stack = []

    for c in text:
        if not stack:
            stack.append(c)
            continue

        if c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    print(f'#{tc} {len(stack)}')

