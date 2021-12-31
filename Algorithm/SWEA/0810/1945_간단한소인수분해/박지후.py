import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    div_by = [2, 3, 5, 7, 11]
    result = {i:0 for i in div_by}
    idx = 0
    q = 1
    while q:
        q, r = divmod(N, div_by[idx])
        if r:
            idx += 1
        else:
            N = q
            result[div_by[idx]] += 1

    print(f'#{tc} {result[2]} {result[3]} {result[5]} {result[7]} {result[11]}')