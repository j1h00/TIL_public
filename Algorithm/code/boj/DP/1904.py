import sys

N = int(sys.stdin.readline())

table = [1, 2]
for i in range(2,N):
    table.append((table[i-2] + table[i-1])%15746)

print(table[N-1])