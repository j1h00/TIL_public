# 다시해야함

K = int(input())
stack = []
field = []
not_field = []
for i in range(6):
    d, l = map(int, input().split())
    if i >= 2 and stack[-2][0] == d:
        not_field.append((d,l))
        not_field.append(stack.pop())
        
    else:
        stack.append((d, l))

