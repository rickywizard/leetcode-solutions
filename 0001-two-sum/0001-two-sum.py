class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):
            temp = target - nums[i]

            if nums[i] in hmap:
                return [hmap[nums[i]], i]

            hmap[temp] = i
