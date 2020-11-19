from PyQt4.QtGui import *
import sys
import edit_test


class Xdialog(QDialog, edit_test.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.btnSave.clicked.connect(self.saveData)
        self.btnCancel.clicked.connect(self.clearData)

    # save button to push
    def saveData(self):
        with open("data.csv", "w") as f:
            s = "%s, %s, %s\n" % (self.editName.text(), self.editCompany.text(), self.editAddr.text())
            f.write(s)
        QMessageBox.information(self, "SAVE", "SUCCESS SAVE")
    
    # cancel button to push
    def clearData(self):
        self.editName.clear()
        self.editCompany.clear()
        self.editAddr.clear()



app = QApplication(sys.argv)
dlg = Xdialog()
dlg.show()
app.exec_()