#run command python -m pytest
from lib.dijkstra import Dijkstra
from lib.node import Node
import math

def add_nodes():
    starting_node = Node("A")
    node_1 = Node("B")
    node_2 = Node("C")
    node_3 = Node("D")
    node_4 = Node("E")
    nodes = [starting_node,node_1,node_2,node_3,node_4]
    algo = Dijkstra(starting_node)
    algo.add_nodes(nodes)
    assert algo.nodes[0] == starting_node
    assert algo.nodes[-1] == node_4
def set_unknown():
    starting_node = Node("A")
    node_1 = Node("B")
    node_2 = Node("C")
    nodes = [starting_node,node_1,node_2]
    algo = Dijkstra(starting_node)
    algo.add_nodes(nodes)
    algo.set_unknown
    assert algo.links_from_starting_node["B"] == [math.inf, None]
    assert algo.links_from_starting_node["C"] == [math.inf, None]
def set_links_from_start():
    starting_node = Node("A")
    node_1 = Node("B")
    node_2 = Node("C")
    node_3 = Node("D")
    starting_node.add_link("B", 5)
    starting_node.add_link("C", 4)
    node_1.add_link("D", 4)
    node_2.add_link("D", 3)
    nodes = [starting_node,node_1,node_2,node_3]
    algo = Dijkstra(starting_node)
    algo.add_nodes(nodes)
    algo.set_unknown()
    algo.set_shortest_path()
    assert algo.links_from_node["A"] == [0, None]
    assert algo.links_from_node["B"] == [5, "A"]
    assert algo.links_from_node["C"] == [4, "A"]
    assert algo.links_from_node["D"] == [7, "B"]
    


