# -*- coding: utf-8 -*-
'''
일반적으로 사용되는 modal 대화 상자
일부 정보 메시지를 표시하고 선택적으로 사용자에게 표준 버튼 중 하나를 클릭하여 응답하도록 요청
각 표준 버튼에는 미리 정의된 캡션, 역활이 있으며 미리 정의된 16진수 숫자를 반환한다.
'''
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QPushButton(w)
   b.setText("Show message!")

   b.move(50,50)
   b.clicked.connect(showdialog)
   w.setWindowTitle("PyQt Dialog demo")
   w.show()
   sys.exit(app.exec_())
	
def showdialog():
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Warning) # setIcon {Question, Information, Warning, Critical}

   msg.setText("This is a message box") # body text
   msg.setInformativeText("This is additional information") # information text
   msg.setWindowTitle("MessageBox demo") # title text
   msg.setDetailedText("The details are as follows:") # Detatil button click to detail text
   # standardButton 원하는 버튼을 표시 함
   msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
   msg.buttonClicked.connect(msgbtn)
   # setDefaultButton() : 버튼을 기본값으로 설정 Enter 키를 누르면 클릭된 신호가 출력
   # setEscapeButton : Escape 키를 누를 경우 버튼일 클릭된 것으로 처리된다.
   retval = msg.exec_()
   print "value of pressed message box button:", retval
	
def msgbtn(i):
   print "Button pressed is:",i.text()
	
if __name__ == '__main__': 
   window()