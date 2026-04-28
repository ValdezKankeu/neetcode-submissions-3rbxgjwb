class Solution:
    def isValid(self, s: str) -> bool:

        openToClost = { ")":"(", "]":"[", "}":"{"}

        stack = []

        for char in s:
            if stack and char in openToClost:
                if stack and stack[-1] ==  openToClost[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False