from lib.dijkstra import Dijkstra
from lib.node import Node

starting_node = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")

starting_node.add_link(node_b, 10)
starting_node.add_link(node_d, 16)
node_b.add_link(node_c, 12)
node_b.add_link(node_d, 18)
node_c.add_link(node_e, 8)
node_d.add_link(node_c, 4)
node_d.add_link(node_e, 14)
nodes = [starting_node, node_b, node_c, node_d,node_e]
algo = Dijkstra(starting_node)
algo.run_algorithm(nodes)
