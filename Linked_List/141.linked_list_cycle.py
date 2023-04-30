

def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow, fast = head, head
    while fast and fast.next:
