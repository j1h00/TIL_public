import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    N_list = [0]*(N+K) # 정류소 리스트
    M_list = map(int, input().split())
    # 충전기가 설치된 정류소는 1로, 나머지는 그대로 0으로 표시한다.
    for i in M_list:
        N_list[i] = 1

    fuel = K # 남은 충전량
    now_idx = 0 # 현재 인덱스 위치
    cnt = 0 # 충전 횟수
    done = False # 도착 여부 판단

    # 충전량이 0 이 아니면
    while fuel:
        now_idx += 1 # 인덱스를 한칸 이동
        fuel -= 1 # 충전량을 1 감소
        if now_idx + fuel >= N: # 만약 현재 위치에서 충전량으로 종점에 도달할 수 있다면
            done = True # 종점에 도착했다고 판단
            break # 루프 탈출
        if N_list[now_idx]: # 만약 현재 위치가 충전기가 설치된 위치라면,
            if 1 in N_list[now_idx+1 : now_idx + fuel + 1]: # 만약 현재 충전량으로 갈 수 있는 거리 내에 충전소가 있다면
                continue # 충전하지 않고 그냥 지나친다
            else:
                fuel = K # 만약 현재 충전량으로 갈 수 있는 거리 내에 충전소가 없다면 충전한다.
                cnt += 1 # 충전 횟수를 늘린다.

    if done:
        print(f'#{tc} {cnt}')
    else:
        print(f'#{tc} 0')



