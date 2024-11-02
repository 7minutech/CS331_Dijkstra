class Node:
    def __init__(self, label):
        self.label = label
        self.links = {}

    # must be able to add a reference 
    # from one node to another
    # A => B => C
    def add_link(self,node,value):
        self.links[node] = value

    
    


        
