"""
    크기가 NxM인 행렬 A와 MxK인 B를 곱할 때 필요한 곱셈 연산의 수는 총 NxMxK번이다. 
    행렬 N개를 곱하는데 필요한 곱셈 연산의 수는 행렬을 곱하는 순서에 따라 달라지게 된다.

    예를 들어, A의 크기가 5x3이고, B의 크기가 3x2, C의 크기가 2x6인 경우에 행렬의 곱 ABC를 구하는 경우를 생각해보자.

    AB를 먼저 곱하고 C를 곱하는 경우 (AB)C에 필요한 곱셈 연산의 수는 5x3x2 + 5x2x6 = 30 + 60 = 90번이다.
    BC를 먼저 곱하고 A를 곱하는 경우 A(BC)에 필요한 곱셈 연산의 수는 3x2x6 + 5x3x6 = 36 + 90 = 126번이다.
    같은 곱셈이지만, 곱셈을 하는 순서에 따라서 곱셈 연산의 수가 달라진다.

    행렬 N개의 크기가 주어졌을 때, 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하는 프로그램을 작성하시오. 
    입력으로 주어진 행렬의 순서를 바꾸면 안 된다.
    항상 순서대로 곱셈을 할 수 있는 크기만 입력으로 주어진다.
"""
N = int(input())

matrix = []
for i in range(N):
    r, c = map(int, input().split())
    matrix.append((r, c))

dp = [[0]*N for _ in range(N)] 
# dp[i][j] 는 matrix[i] 부터 matrix[j] 까지 곱셈했을 때 연산의 최솟값 
# dp[i][j] 는 boj_11066 와 마찬가지로, 
# dp[i][k] + dp[k+1][j] 의 최솟값이다. 
for l in range(1, N):
    for i in range(N-l):
        j = i + l
        dp[i][j] = min([dp[i][k] + dp[k+1][j] + matrix[i][0]*matrix[k][1]*matrix[j][1] for k in range(i, j)])

print(dp[0][N-1])