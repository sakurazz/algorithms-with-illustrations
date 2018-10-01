#! /usr/bin/env python
#coding:utf-8

'''
Kruskal’s algorithm looks at a minimum spanning tree of a weighted connected graph G = ⟨V , E⟩ as an acyclic subgraph with |V | − 1 edges for which the sum of the edge weights is the smallest. 
(It is not difficult to prove that such a subgraph must be a tree.) 
Consequently, the algorithm constructs a minimum spanning tree as an expanding sequence of subgraphs that are always acyclic but are not necessarily connected on the inter- mediate stages of the algorithm.

1) The algorithm begins by sorting the graph’s edges in nondecreasing order of their weights. 
2) Then, starting with the empty subgraph, it scans this sorted list, adding the next edge on the list to the current subgraph if such an inclusion does not create a cycle 
3) and simply skipping the edge otherwise.

Reference: 《Anany: the design and analysis of algorithms(3rd,2011)》

e.g. https://i.imgur.com/g3vFJhR.png

Input:
  
             E
            / 
           /
          / 
         A---- B 
         |    /\
         |   /  \  
         |  /    \ 
         | /      \ 
         |/        \
         C----------D
                    

Output:
  
             E
            / 
           /
          / 
         A---- B 
         |    
         |   
         |  
         | 
         |
         C----------D



'''



'''
    V is used to define Node set. (= vertices & its value)
    V = {'A':'A','B':'B','C':'C','D':'D'}
    When A and B are connected, V is changed to 
    V = {'A':'B','B':'B','C':'C','D':'D'}
    thus,any two points are connnected,their values are the same.
'''
V = dict()
'''
    R means Rank.
    Initial State:R = {'A':'0','B':'0','C':'0','D':'0' } 
    If one vertice is used to be the end of  connections,its value +1.
    Explain:This vertice is used to mark the present Connected Component.
'''
R = dict()

class algorithm():
    
    def __init__(self):
        pass
    #initialize V & R
    def make_set(self,point):
        V[point] = point
        R[point] = 0
    #find out the boss(marker) of the Connected Component.
    def find(self,point):
        if V[point] != point:
            V[point] = self.find(V[point])
        return V[point]
    #Connect two Connected Components and choose a new boss.(marker)
    def union(self,point1,point2):
        r1 = self.find(point1)
        r2 = self.find(point2)
        if R[r1] > R[r2]:
            V[r2] = r1
        else:
            V[r1] = r2
            if R[r1] == R[r2]:
                R[r2] += 1
    #How KRUSKAL works
    def kruskal(self,graph):
        for vertice in graph['vertices']:
            self.make_set(vertice)      #initialization
        MSTree = set()
        edges = list(graph['edges'])
        edges.sort()                    #sort edge lengths from lowest to highest
        for edge in edges:
            weight, vertice1, vertice2 = edge
            if self.find(vertice1) != self.find(vertice2):# not in the same Component
                self.union(vertice1, vertice2)
                MSTree.add(edge)
        return MSTree

if __name__=="__main__":
    graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E'],
        'edges': set([
                      (4, 'A', 'B'),
                      (5, 'A', 'C'),
                      (11, 'B', 'C'),
                      (12, 'B', 'D'),
                      (3,  'A', 'E'),
                      (10, 'C', 'D')
                      ])
    }  # use set(instead list) in edges`s value to remove duplication
    graph2 = {
        'vertices': ['a','b','c','d','e','f'],
        'edge': set([
                    (1,'b','c'),
                    (2,'e','f'),
                    (3,'a','b'),
                    (4,'b','f'),
                    (4,'c','f'),
                    (5,'a','f'),
                    (5,'d','f'),
                    (6,'a','e'),
                    (6,'c','d'),
                    (8,'d','e')
            ])
    }
    arith = algorithm()
    # print arith.kruskal(graph)
    print arith.kruskal(graph2)


