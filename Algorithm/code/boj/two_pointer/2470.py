"""
    KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다. 
    각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다.  
    산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고, 
    알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.

    같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다.
    이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다. 

    산성 용액과 알칼리성 용액의 특성값이 주어졌을 때,
    이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 
    두 용액을 찾는 프로그램을 작성하시오.
"""
import sys
input = sys.stdin.readline

N = int(input())
sol = sorted(list(map(int, input().split()))) # solution 용액 정렬!

l, r = 0, N-1 


answer_l, answer_r = sol[l], sol[r]
close_to_zero = answer_l + answer_r # 둘을 더한 값이 0 에 가까운지 보자!
while l < r:
    mix = sol[l] + sol[r]
    if abs(mix) < abs(close_to_zero): # 만약 0 에 더 가까운 값이 있다면 
        close_to_zero = mix # close to zero 를 업데이트!
        answer_l, answer_r = sol[l], sol[r]
        if mix == 0: # 0 이라면 더이상 찾을 필요 없다. 
            break
    if mix < 0: # 0 보다 작다면, 더 커도 되므로 왼쪽 값을 우측으로 1 이동 
        l += 1
    else:
        r -= 1

print(answer_l, answer_r)
