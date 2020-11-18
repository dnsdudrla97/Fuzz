# -*- coding: utf-8 -*-
# QWidget.setGeometry(xpos, ypos, width, height)
import sys
from PyQt4 import QtGui


def window():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()

    b = QtGui.QPushButton(w)
    b.setText("NAMIN!!")
    b.move(100, 100) # 오른쪽 50px, 추가 및 하방 20px 추가 (x, y) 개념 // 절대위치 임
    # 

    w.setGeometry(10, 20, 300, 200)
    w.setWindowTitle("NAMIN")
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()
