class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        tail = node = head

        while True:
            while node.next.val:
                node.val += node.next.val
                node.next = node.next.next
            if not node.next.next:
                node.next = None
                break
            node = node.next.next
            tail.next = node
            tail = tail.next

        return head
