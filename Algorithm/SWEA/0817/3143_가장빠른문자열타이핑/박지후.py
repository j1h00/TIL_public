import sys
sys.stdin = open('input.txt')

T = int(input())

# # 주어진 테스트 케이스에 대해선 동작하는데, SWEA 제출 시 런타임 에러가 납니다.. help..
# def min_count(A, B):
#     a, b = len(A), len(B)
#     i = 0
#     cnt = 0
#     while i <= a-b:                        # i 는 문자열을 비교할 A 의 인덱스입니다.
#         if A[i] == B[0]:                # (1) 만약 B 의 첫번째 글자와 현재 A의 글자가 같다면
#             j = i
#             for c in B:             # A 와 B 를 하나씩 비교해나갑니다.
#                 if A[j] != c:           # (1-1) 만약 다른 글자가 나온다면,
#                     cnt += 1            # 타이핑 수를 하나 올리고,
#                     i += 1              # 처음 비교하기 시작했던 위치에서 한칸 이동합니다.
#                     break
#                 j += 1
#             else:
#                 cnt += 1                # (1-2) 만약 모두 같은 글자라면, 타이핑 수를 하나 올리고, B 의 크기만큼 이동합니다.
#                 i += b
#         else:
#             cnt += 1                    # (2) 만약 글자가 서로 다르다면, 타이핑 수를 하나 올리고, 다음 글자로 이동합니다.
#             i += 1
#     return cnt


for tc in range(1, T+1):
    A, B = input().split()
    # cnt = min_count(A, B)
    cnt = A.count(B)
    result = cnt + (len(A) - cnt*len(B))

    print(f'#{tc} {result}')