class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char not in pair:
                stack.append(char)    
            else:
                if stack and stack[-1] == pair[char]:
                    stack.pop()
                else:
                    return False

        return stack == []
                
        