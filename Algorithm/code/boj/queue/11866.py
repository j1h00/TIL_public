import sys

NK = sys.stdin.readline().split(" ")
N = int(NK[0])
K = int(NK[1])

queue = list(range(1, N+1))
result = []
size = 0
TOP = 0
while True:
    if size == N-1:
        result.append(queue[TOP])
        break
    if TOP % K == K-1:
        result.append(queue[TOP])
        TOP += 1
        size += 1
    else:
        queue.append(queue[TOP])
        TOP += 1
output = f'{result}'[1:-1]
print('<' + output + '>')