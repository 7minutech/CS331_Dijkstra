#run command python -m pytest
# for this specific file python -m pytest .\test\node_test.py

from lib.node import Node
def test_add_link():
    '''Adds link with value'''
    node =  Node("A")
    node_2 = Node("B")
    node.add_link(node_2,5)
    assert node.links[node_2] == 5
    '''Works with more than 1 link'''
    node_3 = Node("C")
    node_4 = Node("D")
    node.add_link(node_3,4)
    node.add_link(node_4,3)
    assert node.links[node_3] == 4
    assert node.links[node_4] == 3
