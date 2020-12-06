# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import main_rc

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(875, 545)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/main-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(44, 45, 49);"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.stacked = QtGui.QStackedWidget(Dialog)
        self.stacked.setEnabled(True)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.stacked.setFont(font)
        self.stacked.setStyleSheet(_fromUtf8("color: rgb(44, 45, 49);"))
        self.stacked.setObjectName(_fromUtf8("stacked"))
        self.verticalStackedWidgetPage1 = QtGui.QWidget()
        self.verticalStackedWidgetPage1.setObjectName(_fromUtf8("verticalStackedWidgetPage1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalStackedWidgetPage1)
        self.verticalLayout_2.setMargin(20)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.main_img = QtGui.QLabel(self.verticalStackedWidgetPage1)
        self.main_img.setText(_fromUtf8(""))
        self.main_img.setPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/main_img.png")))
        self.main_img.setAlignment(QtCore.Qt.AlignCenter)
        self.main_img.setObjectName(_fromUtf8("main_img"))
        self.verticalLayout_4.addWidget(self.main_img)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(300, -1, 300, -1)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.btn_main_3 = QtGui.QPushButton(self.verticalStackedWidgetPage1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Samsung Sans"))
        font.setPointSize(11)
        self.btn_main_3.setFont(font)
        self.btn_main_3.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 190, 11, 255), stop:1 rgba(251, 86, 7, 255));\n"
"border-radius: 6px;\n"
"\n"
""))
        self.btn_main_3.setObjectName(_fromUtf8("btn_main_3"))
        self.horizontalLayout_8.addWidget(self.btn_main_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setMargin(5)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_program_path = QtGui.QLabel(self.verticalStackedWidgetPage1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Samsung Sans"))
        font.setPointSize(12)
        self.label_program_path.setFont(font)
        self.label_program_path.setObjectName(_fromUtf8("label_program_path"))
        self.verticalLayout_6.addWidget(self.label_program_path)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.edit_main_1 = QtGui.QLineEdit(self.verticalStackedWidgetPage1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Samsung Sans"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.edit_main_1.setFont(font)
        self.edit_main_1.setMouseTracking(True)
        self.edit_main_1.setAutoFillBackground(False)
        self.edit_main_1.setStyleSheet(_fromUtf8("QLineEdit\n"
"{\n"
"    border: 1px solid ;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    color: white;        \n"
"    font: 10pt \"Samsung Sans\";\n"
"        \n"
"}"))
        self.edit_main_1.setDragEnabled(True)
        self.edit_main_1.setReadOnly(True)
        self.edit_main_1.setObjectName(_fromUtf8("edit_main_1"))
        self.horizontalLayout.addWidget(self.edit_main_1)
        self.btn_main_1 = QtGui.QToolButton(self.verticalStackedWidgetPage1)
        self.btn_main_1.setMouseTracking(True)
        self.btn_main_1.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgb(58, 134, 255);\n"
"border-radius: 3px;\n"
""))
        self.btn_main_1.setObjectName(_fromUtf8("btn_main_1"))
        self.horizontalLayout.addWidget(self.btn_main_1)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_sample_path = QtGui.QLabel(self.verticalStackedWidgetPage1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Samsung Sans"))
        font.setPointSize(12)
        self.label_sample_path.setFont(font)
        self.label_sample_path.setObjectName(_fromUtf8("label_sample_path"))
        self.horizontalLayout_7.addWidget(self.label_sample_path)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.edit_main_2 = QtGui.QLineEdit(self.verticalStackedWidgetPage1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Samsung Sans"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.edit_main_2.setFont(font)
        self.edit_main_2.setMouseTracking(True)
        self.edit_main_2.setAutoFillBackground(False)
        self.edit_main_2.setStyleSheet(_fromUtf8("QLineEdit\n"
"{\n"
"    border: 1px solid ;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    color: white;        \n"
"    font: 10pt \"Samsung Sans\";\n"
"        \n"
"}"))
        self.edit_main_2.setDragEnabled(True)
        self.edit_main_2.setReadOnly(True)
        self.edit_main_2.setObjectName(_fromUtf8("edit_main_2"))
        self.horizontalLayout_2.addWidget(self.edit_main_2)
        self.btn_main_2 = QtGui.QToolButton(self.verticalStackedWidgetPage1)
        self.btn_main_2.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgb(58, 134, 255);\n"
"border-radius: 3px;\n"
""))
        self.btn_main_2.setObjectName(_fromUtf8("btn_main_2"))
        self.horizontalLayout_2.addWidget(self.btn_main_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.stacked.addWidget(self.verticalStackedWidgetPage1)
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.textBrowser = QtGui.QTextBrowser(self.page)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Samsung Sans"))
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgb(67, 69, 75);\n"
"border-radius: 5px;\n"
""))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_9.addWidget(self.textBrowser)
        self.verticalLayout_7.addLayout(self.verticalLayout_9)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.progressBar = QtGui.QProgressBar(self.page)
        self.progressBar.setStyleSheet(_fromUtf8("QProgressBar\n"
"{\n"
"    border: 1px solid ;\n"
"    border-color: rgb(67, 69, 75);\n"
"    background-color: rgb(67, 69, 75);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: white;    \n"
"    font: 10pt \"Samsung Sans\";\n"
"        \n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(243, 64, 218, 255), stop:1 rgba(158, 62, 255, 255), stop:2 rgba(97, 62, 254, 255));    \n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}"))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_11.addWidget(self.progressBar)
        self.textBrowser_2 = QtGui.QTextBrowser(self.page)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Samsung Sans"))
        font.setPointSize(10)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgb(67, 69, 75);\n"
"border-radius: 5px;\n"
""))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.verticalLayout_11.addWidget(self.textBrowser_2)
        self.verticalLayout.addLayout(self.verticalLayout_11)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.stacked.addWidget(self.page)
        self.horizontalLayout_4.addWidget(self.stacked)

        self.retranslateUi(Dialog)
        self.stacked.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "FUZZ FUZZ", None))
        self.btn_main_3.setText(_translate("Dialog", "START", None))
        self.label_program_path.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Program Path</span></p></body></html>", None))
        self.btn_main_1.setText(_translate("Dialog", "...", None))
        self.label_sample_path.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Sample Path</span></p></body></html>", None))
        self.btn_main_2.setText(_translate("Dialog", "...", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Samsung Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p></body></html>", None))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Samsung Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

