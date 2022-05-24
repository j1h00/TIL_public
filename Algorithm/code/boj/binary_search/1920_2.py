"""
    N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
    이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
    
    M 개의 X 가 주어진다. 
"""
import sys

N = int(sys.stdin.readline()[:-1])
A_list = sorted([int(_) for _ in sys.stdin.readline()[:-1].split(" ")])

M = int(sys.stdin.readline()[:-1])
search_list = [int(_) for _ in sys.stdin.readline()[:-1].split(" ")]

# 이분탐색 
def binary_search(x, num_list, size):
    start = 0 
    end = size - 1
    while end > start: # 오른쪽 끝이 왼쪽 끝보다 클 경우에만 
        half = (end + start) // 2 # 가운데
        if num_list[half] < x:
            start = half + 1
        else:
            end = half

    if x == num_list[start]: # 만약 찾은 num_list[start] 가 x 와 같다면, 
        return 1
    else:
        return 0
    
for i in search_list:
    print(binary_search(i, A_list, N))