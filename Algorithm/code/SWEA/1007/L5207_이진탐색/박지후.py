import sys
sys.stdin = open('input.txt')


def binary_search(A, m, l, r):
    switch = False # 찾은 경우만 True 로 변경.
    prev = ''

    while l <= r: 
        mid = (l + r) // 2
        if A[mid] == m: # 찾은 경우! 
            switch = True
            break

        elif A[mid] < m: # 오른쪽 확인이 필요한 경우 
            l = mid + 1 # 왼쪽 기준을 mid + 1 로 이동 
            if prev == 'r': # 오른쪽 다음에 오른쪽이 나온 경우 
                switch = False # 조건에 맞지 않는다. 
                break 
            prev = 'r'
        elif A[mid] > m:
            r = mid - 1
            if prev == 'l': # 왼쪽 다음에 왼쪽이 나온 경우 
                switch = False # 조건에 맞지 않는다. 
                break
            prev = 'l'

    return switch 


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split())) 

    cnt = 0
    for m in B: # B 배열의 모든 수에 대해 
        switch = binary_search(A, m, 0, N-1) # 조건을 만족하는지 확인 
        if switch:
            cnt += 1

    print(f'#{tc} {cnt}')