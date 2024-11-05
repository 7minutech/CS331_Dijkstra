#run command python -m pytest 
# for this specific file python -m pytest .\test\dijkstra_test.py

from lib.dijkstra import Dijkstra
from lib.node import Node
import math

def test_add_nodes():
    starting_node = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    node_e = Node("E")
    nodes = [starting_node, node_b, node_c, node_d, node_e]
    algo = Dijkstra(starting_node)
    algo.add_nodes(nodes)
    assert algo.nodes[0] == starting_node
    assert algo.nodes[-1] == node_e

def test_set_unknown():
    starting_node = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    nodes = [starting_node, node_b, node_c]
    algo = Dijkstra(starting_node)
    algo.add_nodes(nodes)
    algo.set_unknown()  
    assert algo.links_from_starting_node[starting_node] == [0, None]
    assert algo.links_from_starting_node[node_b] == [math.inf, None]
    assert algo.links_from_starting_node[node_c] == [math.inf, None]

def test_set_links_from_start():
    starting_node = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    starting_node.add_link(node_b, 5)
    starting_node.add_link(node_c, 4)
    node_b.add_link(node_d, 4)
    node_c.add_link(node_d, 3)
    nodes = [starting_node, node_b, node_c, node_d]
    algo = Dijkstra(starting_node)
    algo.add_nodes(nodes)
    algo.set_unknown()
    algo.set_shortest_path() 
    
  
   
    assert algo.links_from_starting_node[starting_node][0] == 0
    assert algo.links_from_starting_node[starting_node][1] == None
    assert algo.links_from_starting_node[node_b][0] == 5
    assert algo.links_from_starting_node[node_b][1] == starting_node
    assert algo.links_from_starting_node[node_c][0] == 4
    assert algo.links_from_starting_node[node_c][1]  == starting_node
    assert algo.links_from_starting_node[node_d][0] == 7 
    assert algo.links_from_starting_node[node_d][1] == node_c




