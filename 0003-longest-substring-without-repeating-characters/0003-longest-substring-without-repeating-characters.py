class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        memo = {}
        left, right = 0, 0

        while (right < len(s)):
            if s[right] in memo:
                left = max(left, memo[s[right]] + 1)

            if right - left + 1 > maxLen:
                maxLen = right - left + 1

            memo[s[right]] = right
            right += 1

        return maxLen
                
        