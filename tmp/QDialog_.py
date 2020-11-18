import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QPushButton(w)
   b.setText("Hello World!")
   b.move(50,50)
   b.clicked.connect(showdialog)
   w.setWindowTitle("PyQt Dialog demo")
   w.show()
   sys.exit(app.exec_())
	
def showdialog():
   d = QDialog()
   b1 = QPushButton("ok",d)
   b1.move(50,50)
   d.setWindowTitle("Dialog")
   d.setWindowModality(Qt.ApplicationModal)
   d.exec_()
	
if __name__ == '__main__':
   window()

# QDialog

'''
QDialog 위젯은 사용자의 응답을 수집하는데 주로 사용되는 최상위 창을 제시한다.
Modal (부모 창을 차단하는 위치)
Modeless(대화상자 창을 무시할 수 있다.)
두 개로 구성됨
PyQtAPI에는 InputDialog, FileDialog, FontDialog 등 미리 구성된 여러 대화 위젯이 있다.

코드-
대화 상자 창의 모든 속성은 모드인지 모드가 없는지 여부를 결정한다.
대화상자의 버튼 중 하나를 기본값으로 설정할 수있다.
대화상자는 사용자가 escape 키를 누를 때 QDialog.reject() 방법으로 폐기된다.
클릭하면 최상위 레벨 QWidget 창의 추시버튼이 대화상자 창을 생성한다.
대화 상자에는 제목 쵸시줄의 제어 기능이 최소화되고 최대화되지 않는다.
창 모드가 응용 프로그램 모드로 설정되어 있기 떄문에 사용자가 이 대화 상자를 배경에서 해제 할 수 없다.
'''