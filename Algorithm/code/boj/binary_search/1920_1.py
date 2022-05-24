import sys

N = int(sys.stdin.readline()[:-1])
A_list = sorted([int(_) for _ in sys.stdin.readline()[:-1].split(" ")])

M = int(sys.stdin.readline()[:-1])
search_list = [int(_) for _ in sys.stdin.readline()[:-1].split(" ")]

def binary_search(x, num_list, size):
    if len(num_list) == 0:
        return 0 

    half = num_list[size // 2]
    if x == half:
        return 1
    elif x > half:
        return binary_search(x, num_list[half:], size//2)
    elif x < half:
        return binary_search(x, num_list[:half], size//2)
    
for i in search_list:
    print(binary_search(i, A_list, N))

