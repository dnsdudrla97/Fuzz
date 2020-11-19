from PyQt4.QtGui import *
import sys
import sub_

class subDialog(QDialog, sub_.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":        
    app = QApplication(sys.argv)
    dlg = subDialog()
    dlg.show()
    app.exec_()