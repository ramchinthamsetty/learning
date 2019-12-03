"""
    - Implementing Graph Data Structures
    - Adjacency List is the data structure to store relation between Edges and Nodes
    - G = (V,E)
    - |V| - No of Nodes
    - |E| - No of Edges
    - Weighted grah theory will help in finding the shortest path.
    - With weights and Without weights.
"""

class Graph:
    
    def __init__(self):
        self.graph = {
            0:{1:3,3:2}, # Storing weights and edges list V1: {V2, W1}
            1:{7:4},
            2:{3:6, 5:1,7:2},
            3:{4:1,2:6,0:2},
            4:{3:1,8:8},
            5:{2:1,6:8},
            6:{5:8},
            7:{1:4,2:2},
            8:{0:4,4:8}
        }
        return
    
    def get_edges(self):
        """
         - Looping all the edges.
         @return - List of tuples with edges/connections between nodes.
        """
        edges = []
        for key, value1 in self.graph.items():
            for key2,value2 in value1.items():
                edges.append((key, key2, value2)) # (Node1, Node2, Weight)
        return edges
    
    def get_vertices(self):
        """
        - In - self.graph object.
        @return - List of veritices of a graph
        """
        list1 = []
        for key in self.graph.items():
            print(key)
            list1.append(key) # List of Nodes in the Graph
        return list1
    
    def get_path_cost(self, N1, N2):
        """
        - To calculate the cost of Path between nodes.
        """
        N1_edges = self.graph[N1]
        N2_edges = self.graph[N2]
        print(N1_edges, N2_edges)
        N1_edges_list = list(N1_edges.keys())
        N2_edges_list = list(N2_edges.keys())
        print(N1_edges_list)
        print(N2_edges_list)
        if self.graph[N1][N2] is not None:
            print("Direct path exists with cost {}".format(self.graph[N1][N2]))
        # need to implement finding the cost of route, when there is no direct path.
        return 
    
graph = Graph()
print(graph.get_vertices())
print(graph.get_edges())
print(graph.get_path_cost(0, 1))
