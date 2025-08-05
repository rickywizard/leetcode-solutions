class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = {}

        for num in nums:
            if num not in hmap:
                hmap[num] = 1
            else:
                return True
        
        return False