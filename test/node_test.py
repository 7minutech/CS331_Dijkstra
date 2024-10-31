#run command python -m pytest
from lib.node import Node
def test_add_link():
    '''Adds link with value'''
    node =  Node("A")
    node.add_link("B",5)
    assert node.links["B"] == 5
    '''Works with more than 1 link'''
    node.add_link("C",4)
    node.add_link("D",3)
    assert node.link["C"] == 4
    assert node.link["D"] == 5
