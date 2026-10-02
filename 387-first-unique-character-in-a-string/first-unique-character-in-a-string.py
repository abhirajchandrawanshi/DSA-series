class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp={}
        for c in s:
            temp[c]=temp.get(c,0)+1
        i=0
        for c in s:
            if temp[c]<2:
                return i
            i+=1
        return -1
        

