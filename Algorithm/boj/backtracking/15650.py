"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.
"""
import sys

N, M = map(int, sys.stdin.readline().split())

def dfs(stack, N, M):
    if len(stack) == M:
        print(*stack)
    else:
        for i in range(1, N+1):
            if i > stack[-1]:
                stack.append(i)
                dfs(stack, N, M)
                stack.pop()

for i in range(1, N+1):
    dfs([i], N, M)
