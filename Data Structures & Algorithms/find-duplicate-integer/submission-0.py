class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashset=set()

        while n in nums:
            if n in hashset:
                return n
        else:
            return False
