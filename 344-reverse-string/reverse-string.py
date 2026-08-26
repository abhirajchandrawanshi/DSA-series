class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        """
        strt=0
        end=len(s)-1
        while strt<end:
            s[strt],s[end]=s[end],s[strt]
            strt+=1
            end-=1