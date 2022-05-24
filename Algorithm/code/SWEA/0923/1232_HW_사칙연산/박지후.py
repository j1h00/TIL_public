import sys

sys.stdin = open('input.txt')

def postorder(n):
    if values[n]:
        l_cal = postorder(left[n])
        r_cal = postorder(right[n])
        values[n] = str(eval(l_cal + values[n] + r_cal)) # 연산자를 가운데 두고 eval 로 계산합니다.
        return values[n] # 계산 결과를 return 합니다. 
    else: # 자식이 없는 경우   | left[n] = 0     ==>     values[0] = 0     ==> return "" |
        return "" # 빈 문자열을 return 합니다. 

T = 10
for tc in range(1, T+1):
    N = int(input())
    values = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(N): # N 개의 입력을 받아 저장합니다. 
        info = input().split()
        if len(info) > 2: # 입력에 연산자가 있는 경우 
            node, value, l, r = info
            node, l, r = int(node), int(l), int(r)
            values[node] = value
            left[node] = l
            right[node] = r
        else: # 입력에 연산자가 없는 경우 
            node, value = info
            values[int(node)] = value

    postorder(1) # 1번 노드부터 순회하면서 계산합니다.

    print(f'#{tc} {int(float(values[1]))}') 

    