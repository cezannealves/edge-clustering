#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Partition:
    """Partition with efficient union and find operations, with link by rank and path compression"""
    def __init__(self, size, starting_state=None):
        self.num_sets=size
        self._p = list(range(size)) if starting_state == None else starting_state
        self.rank=[1]*size    #rank is an upper bound of height since it changes during path compression
        
        
    def __getitem__(self, key):
        return self.find(key)
        
        
    def find(self, i):
        """returns the set containing i"""
        if self._p[i]!=i:
            self._p[i] = self.find(self._p[i]) # Path compression, doesn't update heigh
            return self._p[i]
        return i
        
        
    def same(self, i, j):
        """test if i and j belong to the same set"""
        return self.find(i) == self.find(j)
    
    
    def union(self, i, j):
        """uninon of the sets containing i and j, if not in the same set already"""
        if not self.same(i,j):
            pi, pj = self.find(i), self.find(j)
            if(self.rank[pi]>self.rank[pj]):
                self._p[pj]=pi
            else:
                self._p[pi]=pj
                if self.rank[pi]==self.rank[pj]: self.rank[pj]+=1
            self.num_sets-=1
    
    def relabeled(self):
        '''returns a relabeled version of the mapping, with set ids in the range [0:num_sets) '''
        unique = list( {self.find(i) for i in range(len(self._p))} )
        mapping=[0]*len(self._p)
        for i in range(len(unique)):
            mapping[unique[i]]=i
        return [mapping[i] for i in self._p]

