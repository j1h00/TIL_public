import sys

N = int(sys.stdin.readline())

triangle = []
for _ in range(N):
    triangle.append([0, *map(int, sys.stdin.readline().split()), 0])

for i in range(1, N):
    for j in range(1, i+2):
        triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[-1]))