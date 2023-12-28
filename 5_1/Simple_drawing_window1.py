import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from Simple_drawing_window import *

class Simple_drawing_window1(Simple_drawing_window):
    def __init__(self):
        Simple_drawing_window.__init__(self)
        self.setWindowTitle("Simple Github Drawing")
        
    def paintEvent(self , e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(0 , 0 , 0))
        p.setBrush(QColor(0 , 50 , 12))
        p.drawPolygon([QPoint(70 , 100) , QPoint(20 , 200) , QPoint(100 , 50) , QPoint( 40 , 90) , QPoint(51 , 700)])
        
        p.end()
        