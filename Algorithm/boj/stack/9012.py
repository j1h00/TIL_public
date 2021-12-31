import sys

K = int(sys.stdin.readline()[:-1])

for i in range(K):
    stack = []
    result = "YES"
    INPUT = sys.stdin.readline()[:-1]
    for i in INPUT:
        if i == ")":
            if len(stack) == 0:
                result = "NO"
                break 
            else:
                stack.pop()
        else:
            stack.append(i)
    if result == "NO":
        print("NO")
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
