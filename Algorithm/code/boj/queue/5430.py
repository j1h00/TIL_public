"""
    선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 
    이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

    함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수이다. 
    배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

    함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 
    예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 숫자를 버리는 함수이다.

    배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.
"""
import sys
from collections import deque


T = int(sys.stdin.readline()[:-1])

for i in range(T):
    p = sys.stdin.readline()[:-1]
    n = int(sys.stdin.readline()[:-1])
    Xs = sys.stdin.readline()[1:-2]
    if Xs == '':
        queue = []
    else:
        queue = deque([int(_) for _ in Xs.split(",")])
    backward = False
    ERROR = False
    
    for RD in p:
        if RD == 'R':
            backward = not backward
        else:
            if len(queue) == 0:
                ERROR = True
                break
            else:
                if backward:
                    queue.pop()
                else:
                    queue.popleft()
    if ERROR:
        print('error')
    elif backward:
        print(str(list(queue)[::-1]).replace(" ", ""))
    else:
        print(str(list(queue)).replace(" ", ""))
            

    