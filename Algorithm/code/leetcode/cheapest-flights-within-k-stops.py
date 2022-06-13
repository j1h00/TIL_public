# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from typing import List

import collections

# return the cheapest price from src to dst with at most k stops. 
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for s, e, p in flights:
            graph[s].append((e, p))

        q = collections.deque([(src, 0, 0)])
        cheapest_prices = [float('inf')] * n
        cheapest_prices[src] = 0 
        while q:
            now, cnt, price = q.popleft()

            for nxt, nxt_price in graph[now]:
                if cheapest_prices[nxt] > price + nxt_price and cnt < k + 1:
                    cheapest_prices[nxt] = price + nxt_price
                    
                    if cnt == k + 1:
                        continue

                    q.append((nxt, cnt + 1, price + nxt_price))
        
        answer = cheapest_prices[dst]
        return answer if answer != float('inf') else -1

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# Dijkstra with heap
# Some explanation.
# The key difference with the classic Dijkstra algo is, we don't maintain the global optimal distance to each node, i.e. ignore below optimization:
## alt ← dist[u] + length(u, v)
##  if alt < dist[v]:
# Because there could be routes which their length is shorter but pass more stops, and those routes don't necessarily constitute the best route in the end. To deal with this, rather than maintain the optimal routes with 0..K stops for each node, the solution simply put all possible routes into the priority queue, so that all of them has a chance to be processed. IMO, this is the most brilliant part.
# And the solution simply returns the first qualified route, it's easy to prove this must be the best route.
import heapq

def findCheapestPrice(self, n, flights, src, dst, k):
    f = collections.defaultdict(dict)
    for a, b, p in flights:
        f[a][b] = p

    heap = [(0, src, k + 1)]
    # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
    # heapq 에 의해, 비용이 큰 경로는 자동적으로 제외된다.
    # Dijkstra 알고리즘 작성 시, heapq 에 집어 넣는 것은 후보이고, 
    # heapq 에서 빼낼 때 비로소 방문했다고 생각하면 이해하기 쉬운 것 같다.
    while heap:
        p, i, k = heapq.heappop(heap) # min-heap => lowest price 
        if i == dst:
            return p
        if k > 0:
            for j in f[i]:
                heapq.heappush(heap, (p + f[i][j], j, k - 1)) 
    return -1


# bfs
class Solution1(object):
	def findCheapestPrice(self, n, flights, src, dst, K):
		graph = collections.defaultdict(list)
		q = collections.deque()
		min_price = float('inf')

		for u, v, w in flights: graph[u].append((w, v))
		q.append((src, 0, 0))
		while q:
			city, stops, price = q.popleft()
			if city==dst:
				min_price = min(min_price, price)
				continue

			if stops<=K and price<=min_price:
				for price_to_nei, nei in graph[city]:
					q.append((nei, stops+1, price+price_to_nei))

		return min_price if min_price!=float('inf') else -1