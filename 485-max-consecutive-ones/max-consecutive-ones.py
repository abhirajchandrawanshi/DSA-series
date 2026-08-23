class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        final=0
        curr=0
        for i in range (len(nums)):
            if nums[i]==1:
                curr+=1
                final=max(curr,final)
            else:
                curr=0
        return final
            
