# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy = ListNode()
        dummy.next = head
        res = dummy
        while dummy.next:

            if dummy.next.val in nums_set:
                tmp = dummy.next.next
                dummy.next.next = None
                dummy.next = tmp
            else:
                dummy = dummy.next

        return res.next
