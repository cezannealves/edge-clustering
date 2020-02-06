#!/usr/bin/env python
# coding: utf-8

# In[1]:


from union_find import Partition

class Kruskall:
    def __init__(self, edges, nnodes, nsets=1):
        """Instantiates and run Kruskal's algorithm on a undirected graph, results ar accessible in the members of the class
        
        Arguments
            nnodes: number of nodes in the graph
            edges: edge list of the form [(w,(n1,n2))], node ids must be contiguous from 0 to 
                nnodes (exclusive). If it has (w,(n1,n2)) it can't have (w,(n2,n1)).
            nsets: the number of MSTs to be left (if possible). If the graph has more connected components than 
        
        Members
            self.tree: edge list of a forest with the number of MSTs equal to 'nsets' or the number of
            connected components of the given graph, whichever is biger.
            self.cost: the cost of the MST
            self.part: Partition of the set of nodes to its MST (  self.part[node_id]= MST_id)
        """
        
        self.cost=0
        self.part = Partition(nnodes)
        self.tree=[]
    
        # kruskal
        edges=sorted(edges)
        for e in edges:
            if self.part.num_sets==nsets: break
            
            i,j = e[1], e[2]
            if not self.part.same(i,j):
                self.tree.append(e)
                self.cost+=e[0]
                self.part.union(i,j)

