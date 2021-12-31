import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    text = input()
    ok = False

    result = []

    for c in text:
        if c in ['(', '{']:
            result.append(c)
        elif c == ')':
            if result and result[-1] == '(':
                result.pop()
            else:
                break

        elif c == '}':
            if result and result[-1] == '{':
                result.pop()
            else:
                break
    else:
         if not result:
            ok = True

    print(f'#{tc} {int(ok)}')

