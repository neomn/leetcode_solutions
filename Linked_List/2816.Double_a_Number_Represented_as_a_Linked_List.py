class Solution(object):
    
    def doubleIt(self, head):
        curr = head 
        if curr.val > 4: 
            head = ListNode(1, head) 
        while curr.next: 
            curr.val = (curr.val * 2 + (curr.next.val > 4)) % 10
            curr = curr.next 
        curr.val = (curr.val * 2) % 10

        return head
