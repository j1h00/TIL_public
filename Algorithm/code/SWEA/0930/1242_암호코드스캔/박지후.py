import sys
from pprint import pprint
sys.stdin = open('input3.txt')

code_dict = {
    '3211':0,
    '2221':1,
    '2122':2,
    '1411':3,
    '1132':4,
    '1231':5,
    '1114':6,
    '1312':7,
    '1213':8,
    '3112':9,
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    HEX_info = []
    for i in range(N):
        HEX = input().strip('0')
        if HEX:
            for prev_HEX in HEX_info:
                if prev_HEX != HEX and prev_HEX in HEX:
                    HEX = HEX.replace(prev_HEX, '0').strip('0')
            if HEX not in HEX_info:
                HEX_info.append(HEX)
    
    BIN_info = []
    for HEX in HEX_info:
        BIN = ''
        for d in HEX:
            BIN += bin(int(HEX, 16))[2:].rstrip()
        
        four = [0, 0, 0, 0]
        now = 1
        for i in range(len(BIN), -1, -1):
            if BIN[i] == now:
                four[]
                
        if BIN not in BIN_info:
            BIN_info.append(BIN)

    for 
    
    


    # info = []
    # for i in range(N):
    #     HEX = input().strip('0') # 0 은 다 버립니다. 
    #     for prev_HEX in info:
    #         if prev_HEX in HEX:
    #             HEX.replace(prev_HEX, '')
    #     if HEX not in info:
    #         info.append(HEX)
    # print(set(info))

    # info_strip = []
    # for HEX in info:
    #     if HEX:
    #         BIN = bin(int(HEX, 16))[2:].rstrip('0') # 코드를 2진수로 바꿉니다.
    #         while len(BIN) % 56:
    #             BIN = '0' + BIN
    #         if BIN not in info:
    #             info_strip.append(BIN)
    

    # final_answer = 0
    # for code in info:
        
    #     verify = 0
    #     temp_answer = 0
    #     length = len(code) // 56
    #     for i in range(1, 9):
    #         now_code = code[7*(i-1) * length : 7*i * length]
    #         short_code = ''
    #         for j in range(7):
    #             short_code += now_code[j * length]
    #             print(tc, info)
    #             print(code)
    #             print(now_code, short_code)
    #         num = code_dict[short_code]
    #         if i%2:
    #             verify += num * 3
    #         else:
    #             verify += num 
    #         temp_answer += num 
        
    #     if verify % 10:  
    #         final_answer += 0
    #     else:
    #         final_answer += temp_answer

    # print(f'#{tc} {final_answer}') 

