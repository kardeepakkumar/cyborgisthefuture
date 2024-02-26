class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')]*n
        prices[src] = 0
        for _ in range(k+1):
            tmp_prices = prices.copy()
            for s, d, p in flights:
                tmp_prices[d] = min(tmp_prices[d], prices[s] + p)
            prices = tmp_prices
        return tmp_prices[dst] if tmp_prices[dst] != float('inf') else -1

# metadata
# relevant-topics bellman-ford, array, graph theory, shortest path
# time-complexity O(N^3) 39.33%
# space-complexity O(N) 98.60%
# language python
# difficulty medium
# date 20240223