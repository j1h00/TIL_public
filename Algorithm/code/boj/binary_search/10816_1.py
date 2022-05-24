"""
    숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 
    정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
"""
# 시간초과 풀이 
import sys

N = int(sys.stdin.readline()[:-1])
A_list = sorted([int(_) for _ in sys.stdin.readline()[:-1].split(" ")])

M = int(sys.stdin.readline()[:-1])
search_list = [int(_) for _ in sys.stdin.readline()[:-1].split(" ")]

# 이분탐색으로 찾는다. 
def binary_search_count(x, num_list, size):
    start = 0 
    end = size - 1
    while end > start:
        half = (end + start) // 2
        if num_list[half] < x:
            start = half + 1
        else:
            end = half

    if num_list[start] != x: # 맞는 수가 없을 경우 
        return 0 

    cnt = 1
    left = start - 1
    right = start + 1
    # 찾은 위치에서 좌우로 한칸 씩 이동하여 몇개가 더 있는지 찾는다. 
    while num_list[left] == x:
        left -= 1
        cnt += 1
        if left < 0:
            break
    while num_list[right] == x:
        right += 1
        cnt += 1
        if right >= size:
            break
    return cnt
    
for i in search_list:
    print(binary_search_count(i, A_list, N))