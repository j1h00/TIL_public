"""
    박성원이 캠프 때 쓸 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다.

    이미 오영식은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다. 
    박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 
    예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)

    편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며, 
    기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 
    그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자. 
    N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 
    이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.
"""
import sys

K, N = [int(_) for _ in sys.stdin.readline()[:-1].split(" ")]
lens = [int(sys.stdin.readline()[:-1]) for i in range(K)] # 현재 가지고 있는 랜선의 길이 

left = 1
right = max(lens)

# 길이 num 으로 정했을 때, 만들 수 있는 랜선의 개수  
def count(num):
    cnt = 0 
    for i in lens:
        cnt += i//num
    return cnt    

while left + 1 < right:
    mid = (left + right) // 2
    cnt = count(mid) # 길이를 mid 로 했을 때, 만들 수 있는 랜선의 개수  
    if cnt >= N: # 랜선의 개수가 N 보다 크거나 같다면, (N 은 필요한 랜선의 개수)
        left = mid
    else:
        right = mid - 1

if count(right) >= N:
    print(right)
else:
    print(left)
