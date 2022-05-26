import sys

def dp(stairs):

    table = []
    table.append(stairs[0])
    table.append(stairs[0] + stairs[1])
    table.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))

    for i in range(3, N):
        table.append(max(stairs[i] + table[i-3] + stairs[i-1], stairs[i] + table[i-2]))
    
    return table[-1]

N = int(sys.stdin.readline())
stairs = []
for i in range(N):
    stairs.append(int(sys.stdin.readline()))

if N > 3:
    print(dp(stairs))
elif N == 1:
    print(stairs[0])
elif N == 2:
    print(stairs[0] + stairs[1])
elif N == 3:
    print(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
    
