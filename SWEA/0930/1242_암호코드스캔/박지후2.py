import sys
from pprint import pprint
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
    
    
    info = []
    for i in range(N):
        HEX = input().strip('0') # 0 은 다 버립니다. 
        if HEX:
            BIN = bin(int(HEX, 16))[2:].rstrip('0') # 코드를 2진수로 바꿉니다.
        
        
        while len(BIN) % 56:
            BIN = '0' + BIN
        if BIN not in info:
            info.append(BIN)


    final_answer = 0
    for code in info:
        
        verify = 0
        temp_answer = 0
        length = len(code) // 56
        for i in range(1, 9):
            now_code = code[7*(i-1) * length : 7*i * length]
            short_code = ''
            for j in range(7):
                short_code += now_code[j * length]
            num = code_dict[short_code]
            if i%2:
                verify += num * 3
            else:
                verify += num 
            temp_answer += num 
        
        if verify % 10:  
            final_answer += 0
        else:
            final_answer += temp_answer

    print(f'#{tc} {final_answer}') 

