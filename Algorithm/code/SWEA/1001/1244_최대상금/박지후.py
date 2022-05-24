import sys
sys.stdin = open('input.txt')

def swap(num, cnt, max_swap):
    global MAX_num
    if cnt == max_swap:
        now_num = int(''.join(num))
        if MAX_num < now_num:
            MAX_num = now_num 
        return 
        
    for i in range(N):
        for j in range(i+1, N):
            num[i], num[j] = num[j], num[i]
            swap(num, cnt + 1, max_swap)
            num[j], num[i] = num[i], num[j]

T = int(input())
for tc in range(1, T+1):
    num, max_swap = input().split()
    max_swap = int(max_swap)
    N = len(num)
    
    num = [i for i in num]
    MAX_num = int(''.join(num))
    cnt = 0
    swap(num, cnt, max_swap)
    print(MAX_num)