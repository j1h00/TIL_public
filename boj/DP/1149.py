import sys

N = int(sys.stdin.readline())

house = []
for _ in range(N):
    house.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    house[i][0] += min(house[i-1][1], house[i-1][2])
    house[i][1] += min(house[i-1][0], house[i-1][2])
    house[i][2] += min(house[i-1][1], house[i-1][0])

print(min(house[-1]))