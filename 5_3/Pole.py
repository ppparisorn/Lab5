import turtle
from Disk import Disk

class Pole(object):
    def __init__(self , name = "" , xpos = 0 , ypos = 0 ,  thick = 20 , length =200):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pythick = thick
        self.plength = length
        self.t = turtle.Turtle()
    
    def showpole(self):
        self.t.penup()
        self.t.goto(self.pxpos , self.pypos)
        self.t.pd()
        self.t.fd(self.pythick/2)
        self.t.lt(90)
        self.t.fd(self.plength)
        self.t.lt(90)
        self.t.fd(self.pythick)
        self.t.lt(90)
        self.t.fd(self.plength)
        self.t.lt(90)
        self.t.fd(self.pythick / 2)
        
    
    def pushdisk(self , disk):
        self.stack.append(disk)
        
        disk.showdisk()
        
        self.pxpos += disk.height
        self.t.pu()
        self.t.goto(self.pxpos , self.pypos)
        self.t.pd()
        
    def popdisk(self):
        x = self.stack.pop()
        x.cleardisk()
        return x
        
        
x = Pole()

x.showpole()
x.pushdisk(Disk("", 0, 0, 50, 200))
turtle.mainloop()