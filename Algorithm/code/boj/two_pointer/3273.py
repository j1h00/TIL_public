"""
    n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. 
    ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 
    자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.
"""
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

cnt = 0

a = sorted(a) # 정렬 
l, r = 0, n-1 # 가장 왼쪽과 오른쪽 인덱스 
cnt = 0
while l < r: 
    now = a[l] + a[r] # 현재 왼쪽과 오른쪽을 더했을 때 
    if now == x: # x 와 같으면, 쌍의 수를 하나 증가 
        cnt += 1
        l += 1 # 좌우 하나씩 가운데로 이동 
        r -= 1
    elif now < x: # 만약 x 보다 작으면, 더 커질 필요가 있으므로 왼쪽 값을 1 우측으로 이동 
        l += 1
    elif now > x:
        r -= 1
        
print(cnt)