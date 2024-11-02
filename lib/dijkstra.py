from lib.node import Node
class Dijkstra:
    def __init__(self, starting_node):
        self.links_from_starting_node = {}
        self.links_from_starting_node[starting_node.label] = [0, starting_node.label]
        self.nodes = []
        self.visited_nodes = []
        self.current_node = starting_node

    def add_nodes(self,node_arr):
        self.nodes = [node.label for node in node_arr]


    