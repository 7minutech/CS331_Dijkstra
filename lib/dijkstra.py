from lib.node import Node
import math
class Dijkstra:
    def __init__(self, starting_node):
        self.links_from_starting_node = {}
        self.links_from_starting_node[starting_node] = [0, None]
        self.nodes = []
        self.visited_nodes = []
        self.current_node = starting_node
        

    # need to keep list of known nodes to set their distance to unknown
    def add_nodes(self,node_arr):
        self.nodes = [node for node in node_arr]

    # need to set the distance of all nodes to infinity b/c 
    # we don't know their distance until it has been traveled
    def set_unknown(self):
        for i in range(1, len(self.nodes)):
            self.links_from_starting_node[self.nodes[i]] = [math.inf, None]
    def set_shortest_path(self):
        while self.current_node:
          
            self.visited_nodes.append(self.current_node)  # current node to visited
          
            # check each node from current node
            for node, weight in self.current_node.links.items():
          
                if self.links_from_starting_node[node][0] > weight + self.links_from_starting_node[self.current_node][0]:
                    self.links_from_starting_node[node] = weight + self.links_from_starting_node[self.current_node][0], self.current_node
            
            #figure out which node to vist next
            self.current_node = None
            fastest_path = math.inf
            
            # find the next path
            for node, weight in self.links_from_starting_node.items():
                if weight[0] < fastest_path and node not in self.visited_nodes:
                    fastest_path = weight[0]
                    self.current_node = node

        return self.links_from_starting_node



    