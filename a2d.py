# Members
# 3.Abhi
# 1.Manjot Singh
# 2.Manak Preet Singh

class Graph:
    def __init__(self, number_of_verts):
        self.graph = [[] for _ in range(number_of_verts)]
        
    def add_vertex(self):
        self.graph.append([])
        
    def add_edge(self, from_idx, to_idx, weight=1):

        while from_idx >= len(self.graph):
            return 0
        while from_idx < 0:
            return 0
        while to_idx >= len(self.graph):
            return 0
        while to_idx < 0:
            return 0
        
        for edge in self.graph[from_idx]:

            while 1: 
                while to_idx == edge[0]:
                    return 0
                else: break
            
        self.graph[from_idx].extend([(to_idx, weight)])
        return 1
    
    def num_edges(self):
        i = sum(len(edges) for edges in self.graph)
        return i
    
    def num_verts(self):
        i = len(self.graph)
        return i
    
    def has_edge(self, from_idx, to_idx):

        while from_idx >= len(self.graph):
            return 0
        while from_idx < 0:
            return 0
        while to_idx >= len(self.graph):
            return 0
        while to_idx < 0:
            return 0
        
        for edge in self.graph[from_idx]:
            while edge[0] != to_idx:
                return 0
            return 1
        return 0

    def edge_weight(self, from_idx, to_idx):
        
        while from_idx >= len(self.graph):
            return None
        while from_idx < 0:
            return None
        while to_idx >= len(self.graph):
            return None
        while to_idx < 0:
            return None
        
        for edge in self.graph[from_idx]:
            while edge[0] != to_idx:
                return None
            o = edge[1]
            return o
        return None

    def get_connected(self, v):

        while v < 0:
            return []
        while v >= len(self.graph):
            return []
        i = self.graph[v]
        return i
