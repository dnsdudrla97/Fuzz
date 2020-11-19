# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\edit_test.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(650, 471)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.editName = QtGui.QLineEdit(Dialog)
        self.editName.setObjectName(_fromUtf8("editName"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.editName)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.editCompany = QtGui.QLineEdit(Dialog)
        self.editCompany.setObjectName(_fromUtf8("editCompany"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.editCompany)
        self.verticalLayout.addLayout(self.formLayout_4)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.editAddr = QtGui.QLineEdit(Dialog)
        self.editAddr.setObjectName(_fromUtf8("editAddr"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.editAddr)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnSave = QtGui.QPushButton(Dialog)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.horizontalLayout.addWidget(self.btnSave, QtCore.Qt.AlignHCenter)
        self.btnCancel = QtGui.QPushButton(Dialog)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout.addWidget(self.btnCancel, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_2.raise_()
        self.label_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "Name", None))
        self.label_4.setText(_translate("Dialog", "Company", None))
        self.label_3.setText(_translate("Dialog", "Address", None))
        self.btnSave.setText(_translate("Dialog", "PushButton", None))
        self.btnCancel.setText(_translate("Dialog", "PushButton", None))

