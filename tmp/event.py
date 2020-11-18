# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
   app = QApplication(sys.argv)
   win = QDialog()
   b1 = QPushButton(win)
   b1.setText("Button1")
   b1.move(50,20)
   b1.clicked.connect(b1_clicked)

   b2 = QPushButton(win)
   b2.setText("Button2")
   b2.move(50,50)
   QObject.connect(b2,SIGNAL("clicked()"),b2_clicked)

   win.setGeometry(100,100,200,100)
   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())

def b1_clicked():
   print "Button 1 clicked"

def b2_clicked():
   print "Button 2 clicked"

if __name__ == '__main__':
   window()

# event 처리시 SIGNAL 을 바탕으로 처리함 
# SLOT : 호출 가능한 모든 python 함수 -> event handler function

# # 가장 일반적인 이벤트 처리방법 
# QtCore.QObject.connect(widget, QtCore.SIGNAL('signalname'), slot_function)

# 시그널이 위젯에 의해 방출 될 때 slot_function 을 초루하는 더 편리한 방법
# widget.signale.connect(slot_function)

# 버튼을 클릭 할 때 함수가 호출된다고 가정하였을 때 클릭된 신호느 ㄴ호출 가능한 함수에 연결된다.
# QtCore.QtObject.connect(button, QtCore.SIGNAL("clicked()"), slot_function)
# button.clicked.connect(slot_function)
