import sys
sys.stdin = open('input.txt')

def backtrack(staff_idx, work_done, p_acc, N):
    global p_max

    # 모든 직원이 할 일을 받은 경우
    if staff_idx == N:
        p_max = max(p_max, p_acc)
        return
    
    # 만약 현재까지의 확률이 이미 최대 확률보다 작은 경우 
    if p_acc <= p_max:
        return 

    # 남은 할일 확인
    work_left = [] 
    for i in range(N):
        if i not in work_done:
            work_left.append(i)

    # 남은 할 일을 staff_idx 번 직원에게 하나 할당.
    for work in work_left:
        backtrack(staff_idx + 1, work_done + [work], p_acc * p_arr[staff_idx][work], N)

# 백분율로 전환
def to_probability(num):
    return int(num) / 100 
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p_arr = []
    for i in range(N):
        p_arr.append(list(map(to_probability, input().split())))

    p_max = 0 # 최대 확률 저장 
    backtrack(0, [], 1, N)

    print(f'#{tc} {p_max*100:.6f}')