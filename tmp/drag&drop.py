# -*- coding: utf-8 -*-
'''
drag and drop은 사용자에게 매우 직관적으로 나타날 수 있다.
사용자가 한 창에서 다른 창으로 개체를 복사하거나 이동할 수 있는 많은 데스크톱에서 사용됨

MIME 기반 드래그 앤 드롭 데이터 전송은 QDrag 클래스 기반으로 한다.
QMimeData 개체는 데이터를 해당 MIME 유형과 연결한다.
클립보드에 저장되어 끌어서 놓기 과정에서 사용된다.
QMimeData 클래스 함수를 사용하면 MIME 유형을 감지하고 편리하게 사용할 수있다.
Tester	Getter	Setter	MIME Types
hasText()	text()	setText()	text/plain
hasHtml()	html()	setHtml()	text/html
hasUrls()	urls()	setUrls()	text/uri-list
hasImage()	imageData()	setImageData()	image/ *
hasColor()	colorData()	setColorData()	application/x-color
'''
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class combo(QComboBox):

   def __init__(self, title, parent):
      super(combo, self).__init__( parent)
	
      self.setAcceptDrops(True)
	# 이벤트의 MIME 데이터에 텍스트가 포함되어 있는지 확인
    # 이벤트의 제안된 작업이 수락되고  텍스트가 ComboBox에 새 항목으로 추가된다.	
   def dragEnterEvent(self, e):
      print e		
      if e.mimeData().hasText():
         e.accept()
      else:
         e.ignore()
			
   def dropEvent(self, e):
      self.addItem(e.mimeData().text())
		
class Example(QWidget):

   def __init__(self):
      super(Example, self).__init__()
		
      self.initUI()
		
   def initUI(self):
      lo = QFormLayout()
      lo.addRow(QLabel("Type some text in textbox and drag it into combo box"))
		
      edit = QLineEdit()
      edit.setDragEnabled(True)
      com = combo("Button", self)
      lo.addRow(edit,com)
      self.setLayout(lo)
      self.setWindowTitle('Simple drag & drop')
		
def main():
   app = QApplication(sys.argv)
   ex = Example()
   ex.show()
   app.exec_()
	
if __name__ == '__main__':
   main()

'''
QWidget 개체는 끌어서 놓기 활동을 지원한다.
!!데이터를 드래그 할 수있도록 허용하는 경우 true로 설정해야 하는 setDragEnabled() 가 있다. 
반면에 위젯은 드래그앤 드롭 이벤트에 응답하여 드래그된 데잍어를 저장해야 한다.

DragEnterEvent: drag action이 들어올 때 대상 위젯으로 전송되는 이벤트를 제공
DragMoveEvent : drag and drop 동작이 진행중일 때 사용
DragLeaveEvent : drag and drop 동작이 위젯을 떠날 때 생성된다.
DropEvent : Drop이 완료될 때 발생한다. 이벤트의 제안 된 작업은 조건부로 수락 또는 거부 될 수 있다.

'''