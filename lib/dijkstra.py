from lib.node import Node
import math
class Dijkstra:
    def __init__(self, starting_node):
        self.links_from_starting_node = {}
        self.links_from_starting_node[starting_node.label] = [0, starting_node.label]
        self.nodes = []
        self.visited_nodes = []
        self.current_node = starting_node

    # need to keep list of known nodes to set their distance to unknown
    def add_nodes(self,node_arr):
        self.nodes = [node.label for node in node_arr]

    # need to set the distance of all nodes to infinity b/c 
    # we don't know their distance until it has been traveled
    def set_unknown(self):
        for i in range(1, len(self.nodes)):
            self.links_from_starting_node[self.nodes[i]] = [math.inf, None]


    