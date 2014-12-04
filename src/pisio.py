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

fromNode = Node("From")
fromNode.x = random.randint(10, 500)
fromNode.y = random.randint(10, 300)
fromNode.radius = 32
fromNode.color = "black"
graph.add(fromNode)

toNode = Node("To")
toNode.x = random.randint(10, 500)
toNode.y = random.randint(10, 300)
toNode.width = 32
toNode.height = 32
toNode.color = "white"
toNode.textColor = "red"
graph.add(toNode)

link = Link(fromNode, toNode, "Link")
link.color = 'green'
graph.add(link)


graph.render()



win.mainloop()
