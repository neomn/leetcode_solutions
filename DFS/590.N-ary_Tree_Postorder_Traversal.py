class Solution:
    def postorder(self, root: "Node") -> List[int]:
        result = []

        # If the root is None, return the empty list
        if root is None:
            return result

        node_stack = [root]  # Stack for traversal
        reverse_stack = []  # Stack to reverse the order

        # Traverse the tree using the node_stack
        while node_stack:
            current_node = node_stack.pop()
            reverse_stack.append(current_node)

            # Push all the children of the current node to node_stack
            for child in current_node.children:
                node_stack.append(child)

        # Pop nodes from reverse_stack and add their values to the result list
        while reverse_stack:
            current_node = reverse_stack.pop()
            result.append(current_node.val)

        return result
