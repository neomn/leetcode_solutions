
def reverseList(head): 
    previous, current = None, head
    while current:
        temp = current.next
        current.next = previous
