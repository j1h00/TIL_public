import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    schedule = [] # 스케쥴을 담는 배열 
    for i in range(N):
        s, e = map(int, input().split())
        schedule.append((s,e))
    
    schedule.sort(key = lambda x: x[1]) # 끝나는 시간에 맞춰서 정렬한다. 
    
    # 현재 기준에서, 가장 빨리 끝나는 회의를 찾는다. 
    cnt = 0
    end = 0 # 현재까지 마친 작업의 종료시간 
    for s, e in schedule: 
        if s >= end: # end 이후에 가능한 시작 시간이 있다면 
            cnt += 1 # 그 작업을 실행한다. 
            end = e # 종료 시간을 업데이트 한다. 

    print(f'#{tc} {cnt}')