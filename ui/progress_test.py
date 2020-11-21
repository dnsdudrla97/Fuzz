import time
from PyQt4 import QtCore, QtGui


styleData="""
QWidget
{
    color: #b1b1b1;
    background-color: #323232;
}
QProgressBar
{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center;
}
QProgressBar::chunk
{
    background-color: #d7801a;
    width: 2.15px;
    margin: 0.5px;
}
QPushButton:pressed
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
}
QComboBox:hover,QPushButton:hover
{
    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}
QPushButton
{
    color: #b1b1b1;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
    border-width: 1px;
    border-color: #1e1e1e;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 12px;
    padding-left: 5px;
    padding-right: 5px;
}"""

class PbWidget(QtGui.QProgressBar):
    def __init__(self, parent=None, total=20):
        super(PbWidget, self).__init__()
        self.setMinimum(1)
        self.setMaximum(total)        
        self._active = False  

    def update_bar(self, to_add_number):
        while True:
            time.sleep(0.01)
            value = self.value() + to_add_number            
            self.setValue(value)
            if value > 50:
                self.change_color("green")
            QtGui.qApp.processEvents()
            if (not self._active or value >= self.maximum()):                
                break
        self._active = False

    def closeEvent(self, event):
        self._active = False

    def change_color(self, color):
        template_css = """QProgressBar::chunk { background: %s; }"""
        css = template_css % color
        self.setStyleSheet(css)

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_layout = QtGui.QVBoxLayout()

        self.pb=PbWidget(total=101)
        self.main_layout.addWidget(self.pb)

        ok_button = QtGui.QPushButton("Press to update Progress Bar")
        ok_button.clicked.connect(self.OK)      
        self.main_layout.addWidget(ok_button)       

        central_widget = QtGui.QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def OK(self):
        self.pb.update_bar(10)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)

    window = MainWindow()
    window.resize(480, 320)
    window.setStyleSheet(styleData)  
    window.show()
    sys.exit(app.exec_())