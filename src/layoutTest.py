import Tkinter
import random
import thread
import time

from graph import Graph
from link import Link
from node import Node
from layout import CircleLayout


win = Tkinter.Tk()
canvas = Tkinter.Canvas(win, bg="white", height=400, width=600)
graph = Graph(canvas)
canvas.pack()

# Create one node

rootNode = Node("root")
rootNode.x = 300
rootNode.y = 200
rootNode.width = 50
rootNode.height = 50
rootNode.color = "black"
graph.add(rootNode)

for i in range(1, 10):
    toNode = Node(str(i))
    toNode.x = random.randint(10, 500)
    toNode.y = random.randint(10, 300)
    toNode.color = "white"
    toNode.textColor = "red"
    graph.add(toNode)
    link = Link(rootNode, toNode, "Link-" + str(i))
    link.color = 'green'
    graph.add(link)

circleLayout = CircleLayout(120)
circleLayout.doLayout(graph.nodes, rootNode)

graph.render()


win.mainloop()
