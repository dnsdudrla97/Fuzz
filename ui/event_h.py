from PyQt4.QtGui import *
import sys
import sub_
import main_

class mainDialog(QDialog, main_.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
    
        self.btn_main_1.clicked.connect(self.openFile)
        self.btn_main_2.clicked.connect(self.openFile)
        self.btn_main_3.clicked.connect(self.enterData)

    def openFile(self, parm):
        # file path 
        fname = QFileDialog.getOpenFileName(self, 'Open file', '*')
        print(parm)
        self.edit_main_1.setText(fname)
        self.edit_main_2.setText(fname)
        print(fname)
        
    def enterData(self):
        # translation sub layout
        print("Loading")
        self.stacked.setCurrentIndex(1)  

if __name__ == "__main__":        
    app = QApplication(sys.argv)
    dlg = mainDialog()
    dlg.show()
    app.exec_()