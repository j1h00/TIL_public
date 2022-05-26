import sys
sys.stdin = open('input.txt')

def postfix_cal(postfix):
    stack = []
    for i in postfix:
        if i not in operator:
            stack.append(i)
        elif i == '.':
            if len(stack) != 1: # 만약 stack 에 두개 이상의 수가 남아있으면 잘못된 식입니다.
                print(f'#{tc} error')
            else:
                print(f'#{tc} {stack.pop()}')
            break
        else:
            if len(stack) < 2: # 숫자가 두개 보다 적으면, 연산이 불가하므로 잘못된 식입니다. 또한 아래 pop 에서 오류가 날 수 있습니다.
                print(f'#{tc} error')
                break
            else:
                one = int(stack.pop())
                two = int(stack.pop())
                if i == '*':
                    stack.append(two * one)
                elif i == '/':
                    stack.append(two // one)
                elif i == '+':
                    stack.append(two + one)
                elif i == '-':
                    stack.append(two - one)

T = int(input())

for tc in range(1, T+1):
    postfix = input().split()
    operator = ['*', '+', '/', '-', '.']

    postfix_cal(postfix)