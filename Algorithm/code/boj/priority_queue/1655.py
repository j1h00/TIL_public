"""
    백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 
    백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 
    만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.
"""
import sys
import heapq


N = int(sys.stdin.readline()[:-1])

left_heap = [] # left_heap 의 최댓값이 중앙값이 되도록 한다. 
right_heap = []

for i in range(1, N+1):
    x = int(sys.stdin.readline()[:-1])
    if len(left_heap) <= len(right_heap): # left_heap, right_heap 의 크기를 동일하게 맞추기 위함.
        heapq.heappush(left_heap, (-x, x)) # left_heap 에는 최대 힙으로 
    else:
        heapq.heappush(right_heap, x) # right_heap 에는 최소 힙으로 
    
    if right_heap and left_heap[0][1] > right_heap[0]: # 만약 right_heap 이 비어있지 않고, left_heap 의 최댓값 보다 right_heap 의 최솟값이 더 작다면 
        left_max = heapq.heappop(left_heap)[1] # left, right 에서 꺼낸다!
        right_min = heapq.heappop(right_heap)
        heapq.heappush(left_heap, (-right_min, right_min)) # 꺼내서 위치 바꿔줌 
        heapq.heappush(right_heap, left_max)

    print(left_heap[0][1])
