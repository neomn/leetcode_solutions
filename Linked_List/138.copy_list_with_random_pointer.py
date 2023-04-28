

def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    oldToCopy = {None: None}
    cur = head
    while cur:
        copy = Node(cur.val)
        oldToCopy[cur] = copy
        cur = cur.next
