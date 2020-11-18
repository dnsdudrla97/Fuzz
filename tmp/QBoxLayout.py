import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def window():
    app = QApplication(sys.argv)
    win = QWidget()

    b1 = QPushButton("Button 1")
    b2 = QPushButton("Button 2")

    vbox = QVBoxLayout() # 위젯을 수직으로 정렬
    vbox.addWidget(b1) # BoxLayout 에 위젯 추가
    vbox.addStretch() # 동적 
    vbox.addWidget(b2) 
    win.setLayout(vbox) # 레이아웃 설정

    win.setWindowTitle("Namin")
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()