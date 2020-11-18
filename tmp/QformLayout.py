# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
   app = QApplication(sys.argv)
   win = QWidget()

   l1 = QLabel("Name")
   nm = QLineEdit()

   l2 = QLabel("Address")
   add1 = QLineEdit()
   add2 = QLineEdit()
   fbox = QFormLayout()
   fbox.addRow(l1,nm)
   vbox = QVBoxLayout()

   vbox.addWidget(add1)
   vbox.addWidget(add2)
   fbox.addRow(l2,vbox)
   hbox = QHBoxLayout()

   r1 = QRadioButton("Male")
   r2 = QRadioButton("Female")
   hbox.addWidget(r1)
   hbox.addWidget(r2)
   hbox.addStretch()
   fbox.addRow(QLabel("sex"),hbox)
   fbox.addRow(QPushButton("Submit"),QPushButton("Cancel"))

   win.setLayout(fbox)
   
   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()


# addRow (QLabel, Qwidget) // 레이블 및 입력 필드를 포함하는 행을 추가한다.
# addRow (QLabel, QLayout) // 두 번째 열에 자식 레이아웃 추가
# addRow (Qwidget) // 두 열에 걸쳐있는 위젯을 추가한다.