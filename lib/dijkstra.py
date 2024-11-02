from lib.node import Node
class Dijkstra:
    def __init__(self, starting_node):
        links_from_starting_node = {}
        links_from_starting_node[starting_node.label] = [0, starting_node.label]
        nodes = []
        visited_nodes = []
        current_node = starting_node
   
    