import sys

K = int(sys.stdin.readline())
stack = []
for i in range(K):
    INPUT = int(sys.stdin.readline()[:-1])
    if INPUT == 0:
        stack.pop()
    else:
        stack.append(INPUT)
print(sum(stack))