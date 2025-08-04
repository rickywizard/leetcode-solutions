class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            print(stones)
            cur = stones.pop() - stones.pop()
            if cur > 0:
                stones.append(cur)
        
        return stones[0] if stones else 0
