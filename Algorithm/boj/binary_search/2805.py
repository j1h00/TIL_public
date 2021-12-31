"""
    목재절단기는 다음과 같이 동작한다. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 
    높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다.
    따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다.

    이때, 적어도 M미터의 나무를 집에 가져가기 위해서 
    절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
"""
import sys

N, M = [int(_) for _ in sys.stdin.readline()[:-1].split(" ")]
trees = [int(_) for _ in sys.stdin.readline()[:-1].split(" ")]

left = 1
right = max(trees)

def cut(num):
    cnt = 0 
    for i in trees:
        sub = i - num  # 절단기 높이를 num 으로 설정했을때, 가질 수 있는 나무 길이  
        if sub > 0:
            cnt += sub
    return cnt    

while left <= right:
    mid = (left + right) // 2
    result = cut(mid)
    if result >= M: # 길이 M 이상의 나무를 원한다. 
        left = mid + 1
    else:
        right = mid - 1

print(right)


