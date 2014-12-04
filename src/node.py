import Tkinter


class Node(object):
    "Visable Object"
    def __init__(self, text=None, x=0, y=0, width=10, height=10, color="black", textColor="white"):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.textColor = textColor
        
    # Center x
    def cx(self):
        return self.x + self.width / 2
    
    # Center y
    def cy(self):
        return self.y + self.height / 2
    
    # How to render itself
    def paint(self, g):    
        g.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)
        g.create_text(self.cx(), self.cy(), text=self.text, fill=self.textColor, anchor=Tkinter.CENTER) 

