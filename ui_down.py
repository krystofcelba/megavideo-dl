# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'down_ui.ui'
#
# Created: Sun Jan 23 15:39:17 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DownDialog(object):
    def setupUi(self, DownDialog):
        DownDialog.setObjectName("DownDialog")
        DownDialog.resize(400, 100)
        self.buttonBox = QtGui.QDialogButtonBox(DownDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 60, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.progressBar = QtGui.QProgressBar(DownDialog)
        self.progressBar.setGeometry(QtCore.QRect(30, 30, 341, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtGui.QLabel(DownDialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 341, 17))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(DownDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DownDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DownDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DownDialog)

    def retranslateUi(self, DownDialog):
        DownDialog.setWindowTitle(QtGui.QApplication.translate("DownDialog", "Download dialog", None, QtGui.QApplication.UnicodeUTF8))

