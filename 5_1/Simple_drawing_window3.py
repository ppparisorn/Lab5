from Simple_drawing_window import Simple_drawing_window

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class Simple_drawing_window3(Simple_drawing_window):
    def __init__(self):
        Simple_drawing_window.__init__(self)
        self.setWindowTitle("Simple Github Drawing 3")
        
    def paintEvent(self , e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(0 , 0 , 0))
        p.setBrush(QColor(0 , 100 , 0))
        p.drawPolygon([QPoint(0 , 0) , QPoint(100 , 0) , QPoint(100 , 100), QPoint(0, 100)])
        
        p.end()

        