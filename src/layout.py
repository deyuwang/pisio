'''

@author: wdy
'''
from math import pi,cos,sin

class CircleLayout():
    def __init__(self,radius=100):
        self.radius = radius
    def doLayout(self, nodes, rootNode):
        #center = self.getNodesCenter(nodes)
        da = 2 * pi / (len(nodes) - 1)
        angle = 0
        for node in nodes:
            if(node == rootNode):
                continue
            node.x = rootNode.x + cos(angle) * self.radius
            node.y = rootNode.y + sin(angle) * self.radius
            angle += da
    def getNodesCenter(self, nodes):
        count = len(nodes)
        xs = 0
        ys = 0
        for node in nodes:
            xs += node.x
            ys += node.y
        return (xs/count, ys/count)