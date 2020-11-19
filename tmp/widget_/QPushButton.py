'''
명령 버튼이 가장 중요함
캡션으로 Save, Open, OK, Yes, No, Cancel 등이 포함된 버튼은 컴퓨터사용자에게 친숙하다.
클릭시 특정 기능을 호출하도록 프로그래밍 할 수있는 버튼을 제공한다.
QAbstractButton class에서 핵심 기능을 계승을 함, 
'''
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
   def __init__(self, parent=None):
      super(Form, self).__init__(parent)
		
      layout = QVBoxLayout()
      self.b1 = QPushButton("Button1")
      self.b1.setCheckable(True) # true로 설정된 경우 버튼의 눌렀다 놓은 상태를 인식한다.
      self.b1.toggle() # 체크 가능한 상태간 전환
      self.b1.clicked.connect(lambda:self.whichbtn(self.b1))
      self.b1.clicked.connect(self.btnstate)
      layout.addWidget(self.b1)
		
      self.b2 = QPushButton()
      self.b2.setIcon(QIcon(QPixmap("python.gif"))) # setIcon : 이미지 파일의 픽스맵으로 형성된 아이콘을 보여준다.
      self.b2.clicked.connect(lambda:self.whichbtn(self.b2))
      layout.addWidget(self.b2)
      self.setLayout(layout)
      self.b3 = QPushButton("Disabled")
      self.b3.setEnabled(False) # false로 설정하면 버튼이 비활성화되므로 클릭해도 신호가 발생하지 않는다.
      layout.addWidget(self.b3)
		
      self.b4 = QPushButton("&Default")
      self.b4.setDefault(True) # 버튼을 기본값으로 설정
      self.b4.clicked.connect(lambda:self.whichbtn(self.b4))
      layout.addWidget(self.b4)
      
      self.setWindowTitle("Button demo")

   def btnstate(self):
      if self.b1.isChecked(): # 버튼의 bool 상태를 반환한다.
         print "button pressed"
      else:
         print "button released"
			
   def whichbtn(self,b):
      print "clicked button is "+b.text()

def main():
   app = QApplication(sys.argv)
   ex = Form()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()