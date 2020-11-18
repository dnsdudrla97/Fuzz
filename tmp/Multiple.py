# -*- coding: utf-8 -*-
'''
GUI 프로그램에는 여러 개의창이 있다.
탭 및 스택 위젯을 사용하면 한 번에 하나의 창을 활성화 할 수있다.
그러나 다른 창보기가 숨겨져 있으므로 이 방법은 유용하지 않다.
여러 창을 동시에 표시하는 한 가지 방법은 독립된 창을 만드는 것이다
이를 SDI (단일 문서 인터페이스)라고 한다.
각 창에는 자체 메뉴 시스템, 도구 모음 등이 있을 수 있으므로더 많은 메모리 리소스가 필요하다.

😉MDI (Multiple Document Interface) 으용ㅇ 프로그램은 더 적은 메모리 리소를 사용한다!
하위 창은 서로 관련하여 주 컨테이너 내부에 배치된다.
컨테이너 위젯은 QMdiArea 라고 부른다.

QMdiArea 위젯은 일반적으로 QMainWindow 개체의 중앙 위젯을 차지한다.
이 영역의 자식 창은 QMdiSubWindow 클래스의 인스턴스이다.

모든 QWidget을 subWindow 객체의 내부 위젯으로 설정할 수있다.
MDI 영역의 하위 창은 계단 식 또는 타일 방식으로 배열할 수 있다.


'''
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MainWindow(QMainWindow):
   count = 0

   def __init__(self, parent=None):
       # QMainWindow 로 구성된 최상위 창에는 메뉴와 MdiArea가 있다.
      super(MainWindow, self).__init__(parent)
      self.mdi = QMdiArea()
      self.setCentralWidget(self.mdi)
      bar = self.menuBar()

      file = bar.addMenu("File")
      file.addAction("New")
      file.addAction("cascade")
      file.addAction("Tiled")
      file.addAction("remove")
      file.triggered[QAction].connect(self.windowaction)
      self.setWindowTitle("MDI demo")

   def windowaction(self, q):
      print "triggered"
      if q.text() == "New":
          MainWindow.count = MainWindow.count+1
          sub = QMdiSubWindow()
          sub.setWidget(QTextEdit())
          sub.setWindowTitle("subwindow"+str(MainWindow.count))
          self.mdi.addSubWindow(sub) # MDI 영역에 새 하우 창으로 위젯 추가
          sub.show()
      # if q.text() == "remove":
        #  self.mdi.removeSubWindow() # 하위 창의 내부 위젯 인 위젯으 ㄹ제거
      if q.text() == "cascade":
          self.mdi.cascadeSubWindows() # MDIArea의 하위 창을 계단식으로 정렬
      if q.text() == "Tiled":
          self.mdi.tileSubWindows() # MDIArea의 하위 창을 바둑판 식으로 배열



def main():
   app = QApplication(sys.argv)
   ex = MainWindow()
   ex.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
    main()

'''
setActiveSubWindow() : 하위 창을 활성화
closeActiveSubWindow() : 활성 하위 창을 닫는다.
subWindowList() : MDI 영역의 하위 창 목록을 반환
setWidget() : QWidget을 QMdiSubwindow 인스턴스의 내부 위젯으로 설정

QMdiArea 객체는 subWindowActivated() 신호를 방출
windowStateChanged() Signal은 QMdisubWindow 객체에 의해 방출된다.

'''