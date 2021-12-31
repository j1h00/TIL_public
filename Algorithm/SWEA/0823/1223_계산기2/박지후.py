import sys

sys.stdin = open('input.txt')

operator = ['(', ')', '+', '-', '*', '/']
isp = { 
    '(':0,
    '+':1,
    '-':1,
    '*':2,
    '/':2
} # in-stack priority

icp = {
    '(':3,
    '+':1,
    '-':1,
    '*':2,
    '/':2
} # in-coming priority

def to_postfix(infix):
    stack = []
    postfix = ""

    for i in infix: # input 을 iterate 합니다. 
        if i not in operator: # 만약 i 가 숫자라면 
            postfix += i # postfix 에 추가합니다. 
        elif not stack: # 만약 stack 에 연산자가 없다면 연산자를 추가합니다. 
            stack.append(i)
        else: # 만약 i 가 연산자 혹은 괄호라면 
            if i == ')': # 만약 닫히는 괄호라면, 열리는 괄호가 나올때 까지 꺼내서 postfix 에 추가합니다. 
                while stack[-1] != '(':
                    postfix += stack.pop()
            else: # 만약 연산자라면, in-stack 과 in-coming 의 연산자 우선순위를 확인합니다. 
                while stack and icp[i] <= isp[stack[-1]]: # 만약 집어 넣어야 할 연산자의 우선순위가 stack top 의 우선순위 보다 낮다면 
                    postfix += stack.pop() # stack 에서 연산자를 꺼내 postfix 에 추가합니다. 
                stack.append(i) # 이제는 집어 넣을 연산자의 우선순위가 크거나 같으므로 stack 에 추가합니다. 
    while stack: # stack 에 쌓여있는 연산자를 postfix 에 차례대로 추가합니다. 
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

T = 10 

for tc in range(1, T+1):
    N = int(input())
    infix = input()
    postfix = to_postfix(infix)
    answer = postfix_cal(postfix)
   
    print(f'#{tc} {answer}')


