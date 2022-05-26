import sys

def switch_click(idx):
    status[idx] = (status[idx] + 1) % 2

N_switch = int(sys.stdin.readline())
status = [0] + list(map(int, sys.stdin.readline().split())) # 스위치 번호가 바로 인덱스가 될 수 있도록 앞에 하나를 더 추가합니다. 
N_student = int(sys.stdin.readline())
# 학생수 만큼 루프를 돌면서 스위치 작업을 진행합니다. 
for i in range(N_student):
    student = tuple(map(int, sys.stdin.readline().split()))
    idx = student[1] 
    if student[0] == 1: # 남학생이라면, 
        while idx <= N_switch: # 스위치 번호를 넘지 않는 선에서 idx 의 배수를 찾아 스위치를 누릅니다.
            switch_click(idx)
            idx += student[1] 
    else: # 여학생이라면 
        switch_click(idx) 
        for j in range(1, N_switch//2): # 왼쪽 오른쪽을 확인하면서 범위 내에서 대칭이면 스위치를 누릅니다. 
            if idx - j >= 1 and idx + j <= N_switch and status[idx-j] == status[idx+j]:
                switch_click(idx-j)
                switch_click(idx+j)
            else:
                break 
    
cnt = 0 
for s in status[1:]:
    print(s, end = " ")
    cnt += 1
    if cnt == 20: # 20 번 출력하고 나면 한줄 띄웁니다.
        print()
        cnt = 0 

