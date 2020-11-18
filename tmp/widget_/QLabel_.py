# -*- coding: utf-8 -*-
'''
QLabel의 객체가 아닌 편집 가능한 텍스트 또는 이미지, 또는 애니메이션 GIF의 영화를 표시하는 자리 표시 자 역할을합니다. 다른 위젯의 니모닉 키로도 사용할 수 있습니다. 일반 텍스트, 하이퍼 링크 또는 서식있는 텍스트를 레이블에 표시 할 수 있습니다.

다음 표는 QLabel 클래스에 정의 된 중요한 메서드를 나열합니다-
'''
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
   app = QApplication(sys.argv)
   win = QWidget() 
	
   l1 = QLabel()
   l2 = QLabel()
   l3 = QLabel()
   l4 = QLabel()
	
   l1.setText("Hello World")
   l4.setText("TutorialsPoint")
   l2.setText("welcome to Python GUI Programming")
	
   # 정렬 (Center, left, Right, Justify)
   l1.setAlignment(Qt.AlignCenter)
   l3.setAlignment(Qt.AlignCenter)
   l4.setAlignment(Qt.AlignRight)
   l3.setPixmap(QPixmap("nm.jpg")) # setPixmap(이미지 표시)
	
   vbox = QVBoxLayout()
   vbox.addWidget(l1)
   vbox.addStretch()
   vbox.addWidget(l2)
   vbox.addStretch()
   vbox.addWidget(l3)
   vbox.addStretch()
   vbox.addWidget(l4)
	
   l1.setOpenExternalLinks(True) # Signal!!
   l4.linkActivated.connect(clicked)
   l2.linkHovered.connect(hovered)
   l1.setTextInteractionFlags(Qt.TextSelectableByMouse)
   win.setLayout(vbox)
	
   win.setWindowTitle("QLabel Demo")
   win.show()
   sys.exit(app.exec_())
	
def hovered():
   print "hovering"
def clicked():
   print "clicked"
	
if __name__ == '__main__':
   window()

# setIndent() : 레이블 텍스트 들여 쓰기 설정
# text() : 레이블의 캡션을 표시한다.
# setText() : 프로그래밍 방식으로 캡션 설정
# selectedText() : 레이블에서 선택한 텍스트를 표시
# textInteractionFlag : TextSelectableByMouse 로 설정해야 함
# setBuddy() : 레이블을 입력 위젯과 연결
# setWordWrap : 레이블에서 줄 바꿈을 활성화 또는 비활성화 한다.

'''
QLabel Class Signal
linkActivated : 포함된 하이퍼 링크가 포함된 레이블을 클릭하면 URL이 열린다.
linkHovered : 이 신호화 관련된 slot 메서드는 하이퍼링크가 포함된 레이블을 마우스로 가리킬때 호출된다.

'''