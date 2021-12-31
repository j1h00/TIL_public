import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    table = [list(input().split()) for _ in range(N)]
    count = 0

    for i in range(100):
        stack = []
        for j in range(100):
            if table[j][i] == '1':
                if not stack:
                    stack.append(table[j][i])
                    continue
                if stack[-1] == '2':
                    if '1' in stack:
                        count += 1
                        stack = []
                        stack.append(table[j][i])
                    else:
                        stack = []
                        stack.append(table[j][i])
                else:
                    stack.append(table[j][i])

            elif table[j][i] == '2':
                stack.append(table[j][i])

            else:
                continue

        if stack and stack[-1] == '2':
            count += 1

    print(f'#{tc} {count}')