from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            self.count -= 1
            return True
        return False

    def connected_components(self):
        return self.count

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)
        
        edges.sort(reverse=True, key=lambda x: x[0])
        
        used_edges = 0

        for edge_type, u, v in edges:
            u -= 1
            v -= 1
            if edge_type == 3:
                if uf_alice.union(u, v) | uf_bob.union(u, v):
                    used_edges += 1
            elif edge_type == 1:
                if uf_alice.union(u, v):
                    used_edges += 1
            elif edge_type == 2:
                if uf_bob.union(u, v):
                    used_edges += 1
        
        if uf_alice.connected_components() > 1 or uf_bob.connected_components() > 1:
            return -1
        
        return len(edges) - used_edges
  
