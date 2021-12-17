import sys
sys.stdin = open('input2.txt')

code_dict = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9,
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    

    # 1 이 있는 줄만 저장합니다. 
    info = []
    for i in range(N):
        temp = input()
        if '1' in temp:
            info.append(temp) 

    # 56자리 코드는 마지막이 무조건 1로 끝나므로, 뒤에서부터 시작하여 1을 찾습니다. 
    end = 0
    for i in range(M-1, -1, -1):
        if info[0][i] == '1':
           end = i
           break 
    start = end - 55 # 56 자리이므로, 시작은 끝에서 -55

    verify = 0 # 검증을 위한 변수입니다. 
    answer = 0 # 정답 출력을 위한 변수입니다. 
    full_code = info[0][start:end+1] # 56 자리 코드를 가져와서 
    for i in range(1, 9):
        now_code = full_code[7*(i-1):7*i] # 7개씩 확인합니다. 
        num = code_dict[now_code]
        if i%2: # 홀수 번째 이면
            verify += num * 3
        else: # 짝수 번째 이면
            verify += num 
        answer += num # 정답 출력을 위한 변수에는 그냥 다 더합니다. 

    if verify % 10: # 검증에 실패하면 (10의 배수가 아니면) 
        answer = 0

    print(f'#{tc} {answer}') 