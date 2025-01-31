from collections import deque 

class UF_Node: # union find node
    def __init__(self, node, parent):
        self.node = node
        self.parent = parent
    
    def get_leader(self):
        if (self.parent == None):
            return self
        self.parent = self.parent.get_leader() # path compression
        return self.parent
    
    # only should be called w/ two leader nodes
    def union(self, uf_node2):
        uf_node2.parent = self

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # construct graph and keep track of which nodes we've connected to so far
        # first time an edge is connects 2 nodes with a connection already, we ret that

        # make nodes
        num_to_node = {}
        for i in range(1, len(edges) + 1):
            num_to_node[i] = UF_Node(i, None)

        # start adding the edges
        for edge in edges:
            n, m = edge
            n_node = num_to_node[n]
            m_node = num_to_node[m]
            
            if (n_node.get_leader() == m_node.get_leader()):
                return edge
            else:
                n_node.get_leader().union(m_node.get_leader())