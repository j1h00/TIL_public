import sys
sys.stdin = open('input.txt')

# 0823 계산기와 동일합니다.. 복붙했습니다..!
def to_postfix(infix):
    stack = []
    postfix = ""

    for i in infix: 
        if i not in operator: 
            postfix += i
        elif not stack:
            stack.append(i)
        else:  
            if i == ')':  
                while stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop() # 남은 '(' 괄호는 필요치 않으므로 버립니다!
            else: 
                while stack and icp[i] <= isp[stack[-1]]:
                    postfix += stack.pop()
                stack.append(i) 
    while stack:
        postfix += stack.pop()

    return postfix

def postfix_cal(postfix):
    stack = []
    for i in postfix:
        if i not in operator: # 연산자가 아니라 숫자라면 stack 에 집어 넣습니다.
            stack.append(i)
        else: # 연산자라면 
            one = int(stack.pop()) # stack 에서 숫자를 두개 꺼내서 연산자에 맞는 연산을 한 뒤 stack 에 다시 넣어줍니다. 
            two = int(stack.pop())
            if i == '*':       
                stack.append(two * one)
            elif i == '/':
                stack.append(two / one)
            elif i == '+':
                stack.append(two + one)
            elif i == '-':
                stack.append(two - one)

    return stack[0]

operator = ['(', ')', '+', '-', '*', '/']
isp = { 
    '(':0,
    '+':1,
    '-':1,
    '*':2,
    '/':2
}

icp = {
    '(':3,
    '+':1,
    '-':1,
    '*':2,
    '/':2
}

T = 10
for tc in range(1, T+1):
    N = int(input())
    infix = input()
    postfix = to_postfix(infix)
    answer = postfix_cal(postfix)
   
    print(f'#{tc} {answer}')
