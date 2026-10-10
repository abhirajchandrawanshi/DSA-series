class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        stack = []

        for char in s:
            if char in valid:
                if not stack or stack[-1] != valid[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return not stack
