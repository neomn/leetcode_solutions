class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def reverse(prev_node, node):
            if not node:
                return prev_node
            temp = node.next
            node.next = prev_node
            return reverse(node, temp)
        
        node = head.next
        head.next = None
        return reverse(head, node)  
