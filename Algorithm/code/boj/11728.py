# 정렬되어있는 두 배열 A와 B가 주어진다. 
# 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오. 

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = []
i = 0
j = 0

while i < N and j < M:
    if A[i] < B[j]:
        answer.append(A[i])
        i += 1 
    else:
        answer.append(B[j])
        j += 1

if i < N:
    # answer += A[i:]
    while i < N:
        answer.append(A[i])
        i += 1
else:
    # answer += B[j:]
    while j < M:
        answer.append(B[j])
        j += 1

print(" ".join(list(map(str, answer))))
# print(" ".join(list(map(str, sorted(A + B)))))

