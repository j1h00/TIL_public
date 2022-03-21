import sys
input = sys.stdin.readline

def dac(A, B, C):

    if B == 1:
        return A % C

    temp = dac(A, B // 2, C)

    if B % 2:
        return temp * temp * A % C
    else:
        return temp * temp % C

def solution():
    A, B, C = map(int, input().split())
    
    print(dac(A, B, C))

solution()