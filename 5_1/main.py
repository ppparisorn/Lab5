from Simple_drawing_window1 import Simple_drawing_window1
from Simple_drawing_window2 import Simple_drawing_window2

from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys

def main():
    app = QApplication(sys.argv)
    
    w1 = Simple_drawing_window1()
    w1.show()
    
    w2 = Simple_drawing_window2()
    w2.show()
    
    app.exec()

if __name__ == "__main__":
      sys.exit(main())