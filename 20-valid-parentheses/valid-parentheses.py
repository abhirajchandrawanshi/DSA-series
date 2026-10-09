class Solution:
    def isValid(self, s: str) -> bool:
        valid ={
            ']':'[',
            ')':'(',
            '}':'{'
        }
        stack=[]
        for chr in s:
            if chr in valid:
                if not stack or stack[-1]!=valid[chr]:
                    return False
                stack.pop()
            else:
                stack.append(chr)
        return not stack