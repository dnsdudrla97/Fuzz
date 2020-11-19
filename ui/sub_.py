# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sub.ui'
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
        Dialog.resize(821, 616)
        Dialog.setStyleSheet(_fromUtf8("background-image: url(:/img/img/main-background.png);"))
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Samsung Sans"))
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(_fromUtf8("border-image: url(:/img/img/sub-background.png);"))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.sub_progress_bar = QtGui.QProgressBar(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Samsung Sans"))
        self.sub_progress_bar.setFont(font)
        self.sub_progress_bar.setStyleSheet(_fromUtf8(""))
        self.sub_progress_bar.setProperty("value", 24)
        self.sub_progress_bar.setObjectName(_fromUtf8("sub_progress_bar"))
        self.verticalLayout_3.addWidget(self.sub_progress_bar)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textBrowser_2 = QtGui.QTextBrowser(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Samsung Sans"))
        font.setPointSize(10)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_2.setStyleSheet(_fromUtf8("border-image: url(:/img/img/sub-background.png);"))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.verticalLayout_2.addWidget(self.textBrowser_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Samsung Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">HIHIHIHIHIHIH</span></p></body></html>", None))

