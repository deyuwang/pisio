import Tkinter


class Link(object):
    ""
    def __init__(self, fromNode, toNode, text="", color="black", textColor="black", width=1):
        self.fromNode = fromNode
        self.toNode = toNode
        self.text = text
        self.color = color
        self.textColor = textColor
    def cx(self):
        return (self.fromNode.cx() + self.toNode.cx()) / 2
    def cy(self):
        return (self.fromNode.cy() + self.toNode.cy()) / 2
    def paint(self, g):
        x1 = self.fromNode.cx()
        y1 = self.fromNode.cy()
    
        x2 = self.toNode.cx()
        y2 = self.toNode.cy()
    
        g.create_line(x1, y1, x2, y2, fill=self.color)
        g.create_text(self.cx(), self.cy(), text=self.text, fill=self.textColor, anchor=Tkinter.CENTER)
