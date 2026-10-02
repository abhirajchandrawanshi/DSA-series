class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(c.lower() for c in s if c.isalnum())
        first=0
        last=len(s)-1
        while first<last:
            if s[first]!=s[last]:
                return False
            first+=1
            last-=1
        return True
        