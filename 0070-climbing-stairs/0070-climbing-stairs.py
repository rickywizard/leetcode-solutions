class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(0, n):
            temp = two
            two = temp + one
            one = temp
        
        return one