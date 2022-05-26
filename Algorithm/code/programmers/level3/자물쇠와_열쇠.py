"""
잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고 
특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.
"""
# 1. 브루트포스 
# => 회전 (4) * 열쇠 돌기의 개수 (?) * 자물쇠 홈의 개수 (?)
# 자물쇠 홈에 열쇠 돌기를 하나 맞춰본 다음 360 도 회전시켜 본다.
# let's try 

# 위의 접근 보다 
# 자물쇠 배열을 열쇠 크기만큼 더 늘린다음에 
# 자물쇠 배열의 모든 위치에서 열쇠를 끼워넣어 보는 편이 좋다. 
from pprint import pprint

def key_in(arr, key, start_x, start_y, N, M): 
    for i in range(M):
        for j in range(M):
            arr[start_x + i][start_y + j] += key[i][j] # key 를 맞춰보자 
    is_match = check(arr, N, M) # check 
    for i in range(M):
        for j in range(M):
            arr[start_x + i][start_y + j] -= key[i][j] # arr 초기화 필요 

    return is_match 
            
def check(arr, N, M):
    for i in range(N):
        for j in range(N):
            if arr[M+i-1][M+j-1] != 1: # N x N 범위가 모두 1인지 확인 (2여도 안됨)
                return False      
    return True 

def solution(key, lock):
    answer = True
    N, M = len(lock), len(key)
    arr = [[0]*(N + (M-1)*2) for _ in range(N + (M-1)*2)]
    for i in range(N):
        for j in range(N):
            arr[M+i-1][M+j-1] = lock[i][j]

    rotated_keys = [key]
    for _ in range(3): # rotate 3 times 
        key = list(zip(*key[::-1]))
        rotated_keys.append(key)

    L = M + N - 1 # 
    for k in rotated_keys: # 모든 회전한 key 에 대해 
        for i in range(L): # (0,0) ~ (M + N - 1, M + N - 1) 까지 모두 확인 
            for j in range(L):
                if key_in(arr, k, i, j, N, M):
                    return True # check 의 결과가 true 이면 return true
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], 	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))