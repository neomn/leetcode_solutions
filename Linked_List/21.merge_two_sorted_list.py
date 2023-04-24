
def mergeTwoLists(list1: listNode, list2: listNode) -> listNode:
             
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        result = ListNode()
        head = result



