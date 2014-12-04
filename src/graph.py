import thread
import time

from link import Link
from node import Node


class Graph():
    def __init__(self, canvas):
        
        # Render target
        self.canvas = canvas
        
        # Containers all nodes for render
        self.nodes = []
        
        # Containers all links for render
        self.links = []
        
        self.bgColor = 'white'
        
        # Start a render loop thread
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
    
