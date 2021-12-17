import sys

sys.stdin = open("input.txt")

T = int(input())

# def get_binary(i):
#     binary_i = ""
#     while i:
#         binary_i = str(i % 2) + binary_i
#         i = i // 2
#     return binary_i

# 위의 이진수 만드는 알고리즘을 응용하여
# i 에 대응하는 부분집합이 N 개의 원소를 가지는지 확인하였습니다.
# 루프가 12번 보다 적게 도는 경우가 많아, 시간 복잡도를 약간 개선할 수 있을 것으로 보입니다.
def get_comb(i, N):
    num = 1
    comb = []
    while i:
        if i % 2:
            comb.append(num)
        i = i // 2
        num += 1
    return comb if len(comb) == N else None     # 원소의 개수가 N 과 다르면 None 을 리턴합니다.

for tc in range(1, T + 1):
    A = list(range(1, 13))
    N, K = map(int, input().split())

    cnt = 0
    for i in range(1 << 12):              # 원소가 12인 집합의 모든 부분집합에 대해 검사합니다.
        subset = get_comb(i, N)           # subset 은 N 개의 원소를 가진 부분집합 중 하나입니다.

        if subset:                        # subset 이 None 이 아니면, 원소의 총합을 구합니다.
            subset_sum = sum(subset)
        else:
            continue

        if subset_sum == K:     # 원소의 총합이 K 라면, 갯수를 하나 올립니다.
            cnt += 1

    print(f'#{tc} {cnt}')