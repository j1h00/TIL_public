import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = 100
    max_height = 100
    dump = int(input())
    b_height = sorted(list(map(int, input().split())))

    for _ in range(dump):
        if b_height[0] == b_height[-1]:
            break
        for j in range(N-1, -1, -1):
            if b_height[j] > b_height[j - 1]:
                b_height[j] -= 1
                break
        for i in range(N):
            if b_height[i] < b_height[i + 1]:
                b_height[i] += 1
                break

    max_min_sub = b_height[-1] - b_height[0]
    print(f'#{tc} {max_min_sub}')