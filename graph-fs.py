# -*- coding: utf-8 -*-  
""" 
Created on Wed Sep 27 00:41:25 2017 
 
@author: my 
"""  
from collections import OrderedDict  
class graph:  
    nodes=OrderedDict({})#有序字典  
  
          
    def toString(self):  
       for key in self.nodes:  
           print key+'邻接点为'+str(self.nodes[key].adj)  
              
    def add(self,data,adj,tag):  
        n=Node(data,adj)  
        self.nodes[tag]=n  
          
        for vTag in n.adj:  
            if self.nodes.has_key(vTag) and tag not in  self.nodes[vTag].adj:  
                self.nodes[vTag].adj.append(tag)  
    visited=[]  
      
    def dfs(self,v):  
        if v not in self.visited:  
            self.visited.append(v)  
            print v  
            for adjTag in self.nodes[v].adj:  
                self.dfs(adjTag)  
    visited2=[]  
    def bfs(self,v):      
        queue=[]  
        queue.insert(0,v)  
        self.visited2.append(v)  
        while(len(queue)!=0):  
            top=queue[len(queue)-1]  
            for temp in self.nodes[top].adj:  
                if temp not in self.visited2:  
                    self.visited2.append(temp)  
                    queue.insert(0,temp)  
            print top  
            queue.pop()  
              
      
class Node:  
    data=0  
    adj=[]  
    def __init__(self,data,adj):  
        self.data=data  
        self.adj=adj  
  
g=graph()  
g.add(0,['e','c'],'a')  
g.add(0,['a','g'],'b')  
g.add(0,['a','e'],'c')  
g.add(0,['a','f'],'d')  
g.add(0,['a','c','f'],'e')  
g.add(0,['d','g','e'],'f')  
g.add(0,['b','f'],'g')  
g.toString()  
print '深度优先遍历的结构为'  
g.dfs('c')  
print '广度优先遍历的结构为'  
g.bfs('c')