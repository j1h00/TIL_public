import sys

sys.stdin = open('input.txt', encoding = 'UTF-8')

T = int(input())

num_dict = {k:v for v, k in enumerate(["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"])}


def quick_sort(A):
    if len(A) <= 1:
        return A

    p = A[len(A) // 2]
    lA = []
    mA = []
    rA = []
    for a in A:
        if num_dict[a] < num_dict[p]:
            lA.append(a)
        elif num_dict[a] > num_dict[p]:
            rA.append(a)
        else:
            mA.append(a)

    return quick_sort(lA) + mA + quick_sort(rA)


for tc in range(1, T+1):
    tc, cnt = map(int, input()[1:].split())
    seq = input().split()
    result = quick_sort(seq)

    print(f'#{tc}')
    print(*result)
