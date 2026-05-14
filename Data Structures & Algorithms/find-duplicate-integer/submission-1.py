class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False