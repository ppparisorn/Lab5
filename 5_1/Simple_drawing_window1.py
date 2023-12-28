import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self , None)
        self.setWindowTitle("Simple Github Drawing")
        
    def paintEvent(self , e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(0 , 0 , 0))
        p.setBrush(QColor(0 , 127 , 0))
        p.drawPolygon([QPoint(70 , 100) , QPoint(20 , 200) , QPoint(100 , 50) , QPoint( 40 , 90) , QPoint(51 , 700)])
        
        p.end()
        