"""
    최소 힙 사용법
"""
import sys
import heapq


N = int(sys.stdin.readline()[:-1])

heap = []

for i in range(N):
    x = int(sys.stdin.readline()[:-1])
    if x:
        heapq.heappush(heap, x)
    else:
        try:
            print(heapq.heappop(heap))
        except IndexError:
            print(0)

