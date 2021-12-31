import sys

K = int(sys.stdin.readline()[:-1])

queue = []
top = 0 
for i in range(K):
    command = sys.stdin.readline()[:-1]
    if command[:4] == 'push':
        queue.append(command.split(" ")[1])
    elif command == 'pop':
        if len(queue) == top:
            print(-1)
        else:
            print(queue[top])
            top += 1
    elif command == 'size':
        print(len(queue)-top)
    elif command == 'empty':
        if len(queue) == top:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(queue) == top:
            print(-1)
        else:
            print(queue[top])
    elif command == 'back':
        if len(queue) == top:
            print(-1)
        else:
            print(queue[-1])
