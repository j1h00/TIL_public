import sys
import heapq


N = int(sys.stdin.readline()[:-1])

heap = []

for i in range(N):
    x = int(sys.stdin.readline()[:-1])
    if x:
        heapq.heappush(heap, (abs(x), x)) # 절댓값으로 비교하여 heap 연산
    else:
        try:
            print(heapq.heappop(heap)[1])
        except IndexError:
            print(0)

