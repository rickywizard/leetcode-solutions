class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = set()

        for num in nums:
            if num in hmap:
                return True
            hmap.add(num)
        
        return False