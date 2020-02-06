#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def find_components(adj_list):
    """Returns the mapping of each node to its connected component in adj_list"""
    
    vis = [0]*len(adj_list)
    comp = [0]*len(adj_list)
    counter=0
    p = []
    
    for i in range(len(adj_list)):
        if not vis[i]:
            p.append(i)
            while (len(p)):
                n=p.pop()
                vis[n]=1
                comp[n]=counter
                for e in adj_list[n]:
                    if not vis[e[2]]:
                        p.append(e[2])
            counter+=1
    return comp

