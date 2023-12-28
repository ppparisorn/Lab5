import turtle

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
        self.t = turtle.Turtle()

    def showdisk(self):
        self.t.fillcolor("gray")
        self.t.begin_fill()
        self.t.penup()
        self.t.setheading(0)
        self.t.goto(self.dxpos, self.dypos)
        self.t.pendown()
        self.t.forward(self.dwidth / 2)
        self.t.left(90)
        self.t.forward(self.dheight)
        self.t.left(90)
        self.t.forward(self.dwidth)
        self.t.left(90)
        self.t.forward(self.dheight)
        self.t.left(90)
        self.t.forward(self.dwidth / 2)
        self.t.end_fill()


    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos

    def cleardisk(self):
        self.t.clear()
        

"""d1 = Disk("", 0, 0, 50, 200)
d1.showdisk()
d1.cleardisk()
turtle.mainloop()"""