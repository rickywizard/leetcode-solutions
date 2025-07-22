class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = 0

        while l <= r:
            mid = l + (r-l)//2

            eatingTime = 0
            for p in piles:
                eatingTime += math.ceil(p/mid)
            
            if eatingTime <= h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1

        return k