from Pole import Pole
from Disk import Disk

class Hanoi(object):
      def __init__(self, n=3, start ="A", workspace = "B", destination = "C"):
            self.startp = Pole(start, 0, 0)
            self.workspacep = Pole(workspace, 150, 0)
            self.destinationp = Pole(destination, 300, 0)
            
            self.startp.showpole()
            self.workspacep.showpole()
            self.destinationp.showpole()
            for i in range(n):
                  self.startp.pushdisk(Disk("d"+str(i), 0, i*150, 20, (n-i)*30))

      def move_disk(self, start, destination):
            disk = start.popdisk()
            destination.pushdisk(disk)
            
      def move_tower(self, n, start, destination, workspace):
            if n == 1:
                  self.move_disk(start, destination)
            else:
                  self.move_tower(n-1, start, workspace, destination)
                  self.move_disk(start, destination)
                  self.move_tower(n-1, workspace, destination, start)

      def solve(self):
            self.move_tower(3, self.startp, self.destinationp, self.workspacep)

h = Hanoi()
h.solve()
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
        
        