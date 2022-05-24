import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num_0, max_swap = input().split()
    max_swap = int(max_swap)

    N = len(num_0)
    comb2 = []
    for i in range(N):
        for j in range(i+1, N):
            comb2.append([i,j])

    num_set = set()
    num_set.add(num_0) 
    for k in range(max_swap):
        tmp = set()
        for num in num_set:
            num = [s for s in num]
            for i, j in comb2:
                num[i], num[j] = num[j], num[i]
                tmp.add(''.join(num)) 
                num[i], num[j] = num[j], num[i]
        num_set = tmp
    
    MAX_num = 0
    for num in num_set:
        now_num = int(''.join(num))
        if MAX_num < now_num:
            MAX_num = now_num
            
    print(f'#{tc} {MAX_num}')


    # 재귀로 풀이시 수행시간이 너무 길어서 포기.. 
    # def swap(num, cnt, max_swap):
    #     global MAX_num
    #     if cnt == max_swap:
    #         now_num = int(''.join(num))
    #         if MAX_num < now_num:
    #             MAX_num = now_num 
    #         return 
            
    #     for i in range(N):
    #         for j in range(i+1, N):
    #             num[i], num[j] = num[j], num[i]
    #             swap(num, cnt + 1, max_swap)
    #             num[j], num[i] = num[i], num[j]