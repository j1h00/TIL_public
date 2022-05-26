import sys

sys.stdin = open("input.txt")

T = int(input())


def fit_count(puzzle):
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N-K+2):
            if sum(puzzle[i][j:j+K]) == K:
                if not puzzle[i][j-1] and not puzzle[i][j+K]:
                    cnt += 1
    return cnt

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [[0]*(N+2)]
    for i in range(N):
        puzzle.append([0, *map(int, input().split()), 0])
    puzzle.append([0]*(N+2))

    result = fit_count(puzzle) + fit_count(list(zip(*puzzle)))

    print(f'#{tc} {result}')
