# 간단한 풀이 
import sys
from collections import Counter

N = int(sys.stdin.readline()[:-1])
A_list = sorted([int(_) for _ in sys.stdin.readline()[:-1].split(" ")])

M = int(sys.stdin.readline()[:-1])
search_list = [int(_) for _ in sys.stdin.readline()[:-1].split(" ")]

C = Counter(A_list) # Counter 를 이용하여 count_dict 형태의 딕셔너리를 만든다. 
print(C)
for i in search_list:
    if i in C:
        print(C[i], end = ' ')
    else:
        print(0, end = ' ')