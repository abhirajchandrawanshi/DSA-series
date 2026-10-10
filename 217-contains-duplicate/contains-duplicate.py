class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # setname= set()
        valid= set()
        for num in nums:
            if num in valid:
                return True
            valid.add(num)
        return False
        