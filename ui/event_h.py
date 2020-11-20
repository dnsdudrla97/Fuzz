from PyQt4.QtGui import *
import sys
import sub_
import main_

class mainDialog(QDialog, main_.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
    
        self.btn_main_1.clicked.connect(self.openProgramPath)
        self.btn_main_2.clicked.connect(self.openSamplePath)
        self.btn_main_3.clicked.connect(self.enterData)

    # program path button
    def openProgramPath(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '*')
        self.edit_main_1.setText(fname)
        print(fname)
        
    # sample path button
    def openSamplePath(self):
        # sample path
        fname = QFileDialog.getOpenFileName(self, 'Open file', '*')
        self.edit_main_2.setText(fname)
        
    def enterData(self):
        # translation sub layout
        print("Loading")
        self.stacked.setCurrentIndex(1)  

if __name__ == "__main__":        
    app = QApplication(sys.argv)
    dlg = mainDialog()
    dlg.show()
    app.exec_()