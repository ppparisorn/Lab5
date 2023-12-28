import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window1(QWidget):
      def __init__(self):
          QWidget.__init__(self , None)
          self.setWindowTitle("Simple Github Drawing")
          self.rabbit = QPixmap("images/rabbit.png")

      def paintEvent(self, e):
            p = QPainter()
            p.begin(self)

            p.setPen(QColor(0 , 0 , 0))
            p.setBrush(QColor(0 , 127 , 0))
            p.drawPolygon([QPoint(70 , 100) , QPoint(20 , 200) , QPoint(100 , 200)])

            p.setPen(QColor(255 , 127 , 0))
            p.setBrush(QColor(255 , 127 , 0))
            p.drawPie(50 , 150 , 100 , 100 , 0 , 180 * 16)

            p.drawPolygon([QPoint(50 , 200) , QPoint(150 , 200) , QPoint(100 , 400)])

            p.drawPixmap(QRect(200 , 100 , 320 , 320) , self.rabbit)
            p.end()

