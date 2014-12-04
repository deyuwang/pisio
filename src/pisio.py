import Tkinter
import random
import thread
import time

from node import Node
from link import Link
from graph import Graph


win = Tkinter.Tk()
canvas = Tkinter.Canvas(win, bg="white", height=400, width=600)
graph = Graph(canvas)
canvas.pack()

#Create one node
def randomNode():
    node = Node()
    node.x = random.randint(10, 500)
    node.y = random.randint(10, 300)
    node.color = "black"
    graph.add(node)
    return node

#Create two nodes and one link
def randomLink():
    fromNode = randomNode()
    toNode = randomNode()
    link = Link(fromNode, toNode)
    graph.add(link)
    return link

def update(no, interval):
    while True:
        randomLink()
        time.sleep(interval)
        
thread.start_new_thread(update, (1,1/10))             


win.mainloop()