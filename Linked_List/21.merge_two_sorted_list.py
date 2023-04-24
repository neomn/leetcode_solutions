
def mergeTwoLists(list1: listNode, list2: listNode) -> listNode:
             
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        result = ListNode()
        head = result

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2


