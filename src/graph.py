import time
import thread

from node import Node
from link import Link

class Graph():
    def __init__(self, canvas):
        self.canvas = canvas
        self.nodes = []
        self.links = []
        self.bgColor = 'white'
        thread.start_new_thread(self.reRender, (1, 1 / 24))  
    def add(self, obj):
        if(type(obj) == Node):
            self.nodes.append(obj)
        elif(type(obj) == Link):
            self.links.append(obj)
    def render(self):
        for link in self.links:
            link.paint(self.canvas)
        for node in self.nodes:
            node.paint(self.canvas)
    def reRender(self, no, interval):
        while True:
            # self.canvas.create_rectangle(0, 0, 600, 400, fill=self.bgColor)
            self.render()
            time.sleep(interval)
    
