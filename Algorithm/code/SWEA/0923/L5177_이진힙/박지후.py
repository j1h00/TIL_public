import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    heap = [0] * (N+1)
    last = 0
    for num in nums:
        last += 1 # last 는 트리의 마지막 노드 번호를 뜻합니다.
        heap[last] = num # 일단 마지막에 노드를 추가합니다.
        c = last
        p = c//2
        while p > 0 and heap[p] > heap[c]: # 만약 루트가 아니고, 부모가 자식보다 크다면 
            heap[p], heap[c] = heap[c], heap[p] # 부모와 자식의 값을 서로 바꿉니다. 
            c = p
            p = c//2 # 한 레벨 위로 올라가서 또 비교해봅니다. 
    
    answer = 0
    while last > 0: # 루트에 도달할 때 까지 
        last = last // 2 
        answer += heap[last] # 조상의 값을 더합니다. 
        

    print(f'#{tc} {answer}')
    