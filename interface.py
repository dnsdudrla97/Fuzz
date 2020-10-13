from PyQt4.QtGui import *
import sys
import test_ui
 
class XDialog(QDialog, test_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
 
app = QApplication(sys.argv)
dlg = XDialog()
dlg.show()
app.exec_()