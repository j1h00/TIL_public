import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    loaded = [0]*N 
    answer = 0
    for i in range(M): # 화물차를 하나씩 보면서,
        tmp_w = 0 # 임시 화물 무게 저장
        tmp_j = 0 # 임시 화물 무게의 인덱스
        for j in range(N): # 화물을 하나씩 확인하면서 
            if not loaded[j] and w[j] <= t[i] and w[j] > tmp_w: # 담을 수 있는 화물 중에 가장 무거운 화물을 찾는다.
                tmp_w = w[j] 
                tmp_j = j
        
        if tmp_w: # 화물의 무게가 0 이 아니라면 ( 담을 수 있는 화물이 있다면 )
            loaded[tmp_j] = 1 # 화물을 중복해서 담는 일 없도록, loaded 에 표시하고, 
            answer += tmp_w # 총 무게에 무게를 추가한다. 
    
    print(f'#{tc} {answer}')