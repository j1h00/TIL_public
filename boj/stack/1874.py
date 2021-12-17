"""
    1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 
    이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
    임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
    있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 
    이를 계산하는 프로그램을 작성하라.
"""
import sys

K = int(sys.stdin.readline())

permanent = []
stack = ['start']
sequence = []
plus_minus = []
now = int(sys.stdin.readline()[:-1])
n = 1 # 1 ~ N 까지 수에 대해 하나씩 push or pop 
while len(sequence) < K: # sequence 길이가 K 가 될 때 까지 
    if stack[-1] == now: # 만약 stack 의 끝 수가 now 와 같다면 
        sequence.append(stack.pop()) # stack 에사 pop 하여 sequence 에 넣는다 
        plus_minus.append("-") # pop 을 했으므로, '-' 
        if len(sequence) == K: # 만약 sequence 길이가 K 라면 멈춰도 된다. 
            break
        now = int(sys.stdin.readline()[:-1]) # 다음 now 를 찾는다. 
        continue

    if n > K: # n 이 K 보다 크다면 수열을 만들 수 없는 경우이다. 
        plus_minus = ["NO"]
        break 

    stack.append(n) # 만약 stack 의 숫자와 now 가 다르다면 push 
    plus_minus.append("+")
    n += 1 # 

for i in plus_minus:
    print(i)

