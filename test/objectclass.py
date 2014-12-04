'''
@author: wdy
'''

class Node():
    type = "Node" # A class attribute
    def __init__(self,name=None):
        self.name = name

node = Node()

print getattr(node, 'name')

setattr(node, "name", "node")

print node.name
print node.type == Node.type