class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):
            temp = target - nums[i]

            if temp in hmap:
                return [hmap[temp], i]

            hmap[nums[i]] = i
