class Solution:
    def removeStones(self, stones):
        uf = self.UnionFind(
            20002
        )  # Initialize UnionFind with a large enough range to handle coordinates

        # Union stones that share the same row or column
        for x, y in stones:
            uf._union_nodes(
                x, y + 10001
            )  # Offset y-coordinates to avoid conflict with x-coordinates

        return len(stones) - uf.component_count

    # Union-Find data structure for tracking connected components
    class UnionFind:
        def __init__(self, n):
            self.parent = [-1] * n  # Initialize all nodes as their own parent
            self.component_count = (
                0  # Initialize the count of connected components
            )
            self.unique_nodes = (
                set()
            )  # Initialize the set to track unique nodes

        # Find the root of a node with path compression
        def _find(self, node):
            # If node is not marked, increase the component count
            if node not in self.unique_nodes:
                self.component_count += 1
                self.unique_nodes.add(node)

            if self.parent[node] == -1:
                return node
            self.parent[node] = self._find(self.parent[node])
            return self.parent[node]

        # Union two nodes, reducing the number of connected components
        def _union_nodes(self, node1, node2):
            root1 = self._find(node1)
            root2 = self._find(node2)

            if root1 == root2:
                return  # If they are already in the same component, do nothing

            # Merge the components and reduce the component count
            self.parent[root1] = root2
            self.component_count -= 1
