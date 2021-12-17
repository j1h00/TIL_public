import sys

K = int(sys.stdin.readline()[:-1])

queue = list(range(1, K+1))
top = 0 
for i in range(K-1):
    top += 1
    queue.append(queue[top])
    top += 1

print(queue[top])
