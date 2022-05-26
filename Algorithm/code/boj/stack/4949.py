import sys

while True:
    INPUT = sys.stdin.readline()[:-1]
    if INPUT == '.':
        break
    stack = []
    result = "yes"
    pair = {
        ']':'[',
        ')':'('
    }
    for i in INPUT:
        if i in ['[', '(']:
            stack.append(i)
        elif i in [']', ')']:
            if len(stack) == 0:
                result = 'no'
                break
            elif pair[i] != stack[-1]:
                result = 'no'
                break
            else:
                stack.pop()
    if len(stack) > 0:
        result = 'no'
    print(result)
        