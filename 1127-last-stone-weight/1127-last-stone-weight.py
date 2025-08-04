class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            cur = a - b
            if cur < 0:
                heapq.heappush(stones, cur)
            
        return stones[0] * -1 if stones else 0
