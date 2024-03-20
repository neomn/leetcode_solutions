class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pointer = list1
        for _ in range(a-1):  
            pointer = pointer.next
        anode = pointer
        for _ in range(b-a+2): 
            pointer = pointer.next
        bnode = pointer

        anode.next = list2
        pointer = list2
        while pointer.next:  
            pointer = pointer.next
        pointer.next = bnode
        return list1
