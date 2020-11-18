# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget() # QWidget 최상위 창을 만든다. (Qlabel 개체에 추가)
    b = QtGui.QLabel(w)
    b.setText('NAMIN') # setText (라벨의 캡션을 "설정")
    w.setGeometry(100, 100, 200, 50) # 창의 크기와 위치를 정의
    b.move(50, 10)
    w.setWindowTitle("PyQt")
    w.show()
    sys.exit(app.exec_()) # 애플리케이션의 메인 루프





if __name__ == "__main__":
    window()