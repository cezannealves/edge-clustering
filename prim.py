#!/usr/bin/env python
# coding: utf-8

# In[1]:


import heapq

class Prim:
    def __init__(self, adj_list, start_n=0):
        """Instantiate and run Prims's algorithm on a undirected graph, results are accessible in the members of the class
        
        Arguments
            adj_list: adjacency list in the form [[(w,(n1,n2))]]
            start_n=0: starting node for the algorithm
        
        Members
            cost: the cost of the MST
            tree_adj: the MST inf form of adjacency list
            tree_edges: the MST inf form of edge list
        """
        self.cost=0
        self.tree_edges=[]
        self.tree_adj=[[]for i in range(len(adj_list))]
        
        nnodes = len(adj_list)
        taken = [0]*nnodes
        ntaken = 0
        q=[]
        
        def process(n): # inside __init__ because it needs its arguments
            nonlocal taken, ntaken
            taken[n]=1; ntaken+=1
            for e in adj_list[n]:
                if not taken[e[2]]:
                    heapq.heappush(q, e)
        
        while(ntaken!=nnodes):          # this is to guarantee MST of all connected components
            
            process(start_n)
            
            while len(q)>0:
                
                e = heapq.heappop(q)
                n=e[2]
                
                if not taken[n]:
                    self.cost+=e[0]
                    self.tree_edges.append(e)
                    self.tree_adj[e[1]].append(e)
                    self.tree_adj[e[2]].append((e[0], e[2], e[1]))
                    process(n)
                    
            if ntaken!=nnodes:
                start_n = taken.index(0)
        

