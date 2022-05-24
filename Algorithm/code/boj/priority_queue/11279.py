"""
    # 최대 힙 사용법
    널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

    배열에 자연수 x를 넣는다.
    배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
    프로그램은 처음에 비어있는 배열에서 시작하게 된다.
"""
import sys
import heapq


N = int(sys.stdin.readline()[:-1])

heap = []

for i in range(N):
    x = int(sys.stdin.readline()[:-1])
    if x:
        heapq.heappush(heap, -x) # python heap module 은 최소 힙이 default 이므로, 음수 처리 하여 집어넣는다. 
    else: # x 가 0 인 경우 
        try:
            print(heapq.heappop(heap)*(-1)) # 가장 큰 값을 출력한다. 
        except IndexError: # heap 이 비어있는 경우엔 
            print(0)

