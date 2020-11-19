# -*- coding: utf-8 -*-
'''
QLineEdit :
입력 필드, 한 줄의 텍스트를 입력 할 수 있는 Box를 제공한다.
여러 줄 텍스트를 입력하려면 QTextEdit 개체가 필요하다.

'''
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
   app = QApplication(sys.argv)
   win = QWidget()
	
   e1 = QLineEdit()
   e1.setValidator(QIntValidator()) #  유효성 검사 규칙을 설정한다.
   # QintValidator() : 정수만 입력 가능
   # QDoubleValidator : 지정된 소수로 제한된 수의 분할 부분
   # QRegexpValidator : Regex 식에 대한 입력을 확인한다.

   e1.setMaxLength(4) # 입력에 대한 최대 문자 수를 설정 한다. (4)
   e1.setAlignment(Qt.AlignRight) # 정렬 (Left, Right, Center, Justify)
   e1.setFont(QFont("Arial",20))
	
   e2 = QLineEdit()
   e2.setValidator(QDoubleValidator(0.99,99.99,2))
	
   flo = QFormLayout()
   flo.addRow("integer validator", e1)
   flo.addRow("Double validator",e2)
	
   e3 = QLineEdit()
   e3.setInputMask('+99_9999_999999') # 입력시 문자 조합 마스크 적용
   flo.addRow("Input Mask",e3)
	
   e4 = QLineEdit()
   e4.textChanged.connect(textchanged)
   flo.addRow("Text changed",e4)
	
   e5 = QLineEdit()
   e5.setEchoMode(QLineEdit.Password) # 상자 안의 텍스트 모양을 제어한다. 
   # Normal, NoEcho, Password, PasswordEchoOnEdit
   flo.addRow("Password",e5)
	
   e6 = QLineEdit("Hello Python")
   e6.setReadOnly(True) # 텍스트 상자를 편집할 수 없도록 설정
   flo.addRow("Read Only",e6)
	
   e5.editingFinished.connect(enterPress)
   win.setLayout(flo)
   win.setWindowTitle("PyQt")
   win.show()
	
   sys.exit(app.exec_())

def textchanged(text):
   print "contents of text box: "+text
	
def enterPress():
   print "edited"

if __name__ == '__main__':
   window()

''' method 

clear() : 콘텐츠 제거

'''

''' signal
cursorPostionChanged() : 커서 움직임
editingFinished() : Enter 키를 누르거나 , 입력 필드 에서 나갔을 경우
returnPressed() : Enter 키를 눌렀을 때
selectionChanged() : 선택한 텍스트가 변경될 때 마다.
textChanged() : 상자의 텍스타가 입려 또는 프로그램적 수단에 의해 변경됨에 따라
textEdited() : 텍스트를 입력했을 때


'''