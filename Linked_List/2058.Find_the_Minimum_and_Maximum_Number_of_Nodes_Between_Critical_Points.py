class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_dist = float('inf')
        max_dist = -1

        prev_node = head
        head = head.next
        if head.next:
            next_node = head.next
        else:
            return [-1, -1]

        first_critical_node_position = 0
        prev_critical_node_position = 0
        position = 1
        while next_node:
            if (prev_node.val < head.val and next_node.val < head.val) or \
               (head.val < prev_node.val and head.val < next_node.val):
                if not first_critical_node_position:
                    first_critical_node_position = position
                if not prev_critical_node_position:
                    prev_critical_node_position = position
                else:
                    min_dist = min( min_dist, position - prev_critical_node_position)
                    prev_critical_node_position = position
            position += 1
            prev_node = head
            head = next_node
            next_node = next_node.next

        single_or_no_critical_node = bool(first_critical_node_position == prev_critical_node_position)
        max_dist = prev_critical_node_position - first_critical_node_position
        return [-1, -1] if single_or_no_critical_node else [min_dist, max_dist]
