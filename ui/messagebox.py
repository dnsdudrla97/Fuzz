# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\messagebox.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(664, 384)
        Form.setStyleSheet(_fromUtf8("background-color: rgb(44, 45, 49);"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 100)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Samsung Sans"))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.textbrowser_md5 = QtGui.QTextBrowser(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textbrowser_md5.sizePolicy().hasHeightForWidth())
        self.textbrowser_md5.setSizePolicy(sizePolicy)
        self.textbrowser_md5.setStyleSheet(_fromUtf8("border: 1px solid ;\n"
"border-color: rgb(44, 45,49);\n"
"border-radius: 10px;\n"
"color: white;        \n"
"font: 10pt \"Samsung Sans\";\n"
""))
        self.textbrowser_md5.setObjectName(_fromUtf8("textbrowser_md5"))
        self.horizontalLayout_4.addWidget(self.textbrowser_md5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Samsung Sans"))
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.textbrowser_crash = QtGui.QTextBrowser(Form)
        self.textbrowser_crash.setStyleSheet(_fromUtf8("border: 1px solid ;\n"
"border-color: rgb(44, 45,49);\n"
"border-radius: 10px;\n"
"color: white;        \n"
"font: 10pt \"Samsung Sans\";\n"
""))
        self.textbrowser_crash.setObjectName(_fromUtf8("textbrowser_crash"))
        self.horizontalLayout_3.addWidget(self.textbrowser_crash)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 70, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_close_m = QtGui.QPushButton(Form)
        self.btn_close_m.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgb(255, 81, 81);\n"
"border-radius: 6px;\n"
"font: 10pt \"Samsung Sans\";"))
        self.btn_close_m.setObjectName(_fromUtf8("btn_close_m"))
        self.horizontalLayout.addWidget(self.btn_close_m)
        self.btn_report_m = QtGui.QPushButton(Form)
        self.btn_report_m.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgb(70, 96, 254);\n"
"border-radius: 6px;\n"
"font: 10pt \"Samsung Sans\";"))
        self.btn_report_m.setObjectName(_fromUtf8("btn_report_m"))
        self.horizontalLayout.addWidget(self.btn_report_m)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">MD5 Hash</span></p></body></html>", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Crash Path</span></p></body></html>", None))
        self.textbrowser_crash.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Samsung Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Gulim\'; font-size:9pt; font-weight:200;\"><br /></p></body></html>", None))
        self.btn_close_m.setText(_translate("Form", "CLOSE", None))
        self.btn_report_m.setText(_translate("Form", "REPORT", None))

