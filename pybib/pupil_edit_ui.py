# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pupil_edit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(501, 296)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deleteButton = QtWidgets.QPushButton(Dialog)
        self.deleteButton.setAutoDefault(False)
        self.deleteButton.setFlat(False)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.nameEdit = QtWidgets.QLineEdit(self.groupBox)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.nameEdit)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.gradeEdit = QtWidgets.QLineEdit(self.groupBox)
        self.gradeEdit.setObjectName("gradeEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.gradeEdit)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.genderCombo = QtWidgets.QComboBox(self.groupBox)
        self.genderCombo.setObjectName("genderCombo")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.genderCombo)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.prenameEdit = QtWidgets.QLineEdit(self.groupBox)
        self.prenameEdit.setObjectName("prenameEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.prenameEdit)
        self.idEdit = QtWidgets.QLineEdit(self.groupBox)
        self.idEdit.setEnabled(False)
        self.idEdit.setObjectName("idEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.idEdit)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.setStretch(1, 5)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Schüler"))
        self.deleteButton.setText(_translate("Dialog", "Löschen"))
        self.groupBox.setTitle(_translate("Dialog", "Schüler"))
        self.label.setText(_translate("Dialog", "ID"))
        self.label_2.setText(_translate("Dialog", "Nachname"))
        self.label_3.setText(_translate("Dialog", "Klasse"))
        self.label_4.setText(_translate("Dialog", "Geschlecht"))
        self.label_5.setText(_translate("Dialog", "Vorname"))

