import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def window():
   app = QApplication(sys.argv)
   win = QWidget()
   grid = QGridLayout()
	
   for i in range(1,5):
      for j in range(1,5):
         grid.addWidget(QPushButton("B"+str(i)+str(j)),i,j)
			
   win.setLayout(grid)
   win.setGeometry(100,100,200,100)
   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()

# addWidget (Qwidget, int r, int c) // 지정된 행과 열에 위젯을 추가한다.
# addWidget (Qwidget, inr r, int c, int rowspan, int columnspan) // 지정된 행과 열에 지정된 너비 및 / 또는 높이를 갖는 위젯을 추가한다.
# addLayout(QLayout, int r, int c) // 지정된 행과 열에 레이아웃 개체를 추가한다.
