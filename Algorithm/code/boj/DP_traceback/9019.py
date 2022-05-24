"""
    네 개의 명령어 D, S, L, R 을 이용하는 간단한 계산기가 있다. 
    이 계산기에는 레지스터가 하나 있는데, 이 레지스터에는 0 이상 10,000 미만의 십진수를 저장할 수 있다. 
    각 명령어는 이 레지스터에 저장된 n을 다음과 같이 변환한다. 
    n의 네 자릿수를 d1, d2, d3, d4라고 하자(즉 n = ((d1 x 10 + d2) x 10 + d3) x 10 + d4라고 하자)

    D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
    S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
    L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
    R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
"""
from collections import deque

def D(n):
    return 2*n % 10000, 'D'

def S(n):
    return 9999 if n == 0 else n-1, 'S'

def L(n):
    return int(n % 1000 * 10 + n / 1000), 'L' # str 으로 형변환 시 시간초과 우려 

def R(n):
    return int(n % 10 * 1000 + n // 10), 'R'


T = int(input())

for tc in range(T):
    A, B = map(int, input().split())
    visited = [0]*10000
    command = [0]*10000

    q = deque()
    q.append(A)
    visited[A] = 1

    while q:
        now = q.popleft()
        if now == B:
            break 

        for nxt, C in [D(now), S(now), L(now), R(now)]:
            if 0 <= nxt <= 9999 and not visited[nxt]:
                q.append(nxt)
                visited[nxt] = 1
                command[nxt] = (now, C)
    
    answer = ''
    now = B
    while now != A:
        answer = command[now][1] + answer # 거꾸로 담아야한다. 
        now = command[now][0]
    
    print(answer)

