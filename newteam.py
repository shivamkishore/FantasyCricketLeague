# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newteam.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(407, 260)
        Dialog.setStyleSheet("background-color: rgb(92, 219, 209);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, -20, 401, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 50, 210, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.team_name = QtWidgets.QLineEdit(self.frame)
        self.team_name.setGeometry(QtCore.QRect(90, 91, 221, 41))
        self.team_name.setObjectName("team_name")
        self.team_name.setStyleSheet("background-color: rgb(255,255,255);")
        self.savename = QtWidgets.QPushButton(self.frame)
        self.savename.setGeometry(QtCore.QRect(140, 160, 93, 28))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.savename.setFont(font)
        self.savename.setStyleSheet("font: italic 8pt \"MS Sans Serif\";")
        self.savename.setStyleSheet("background-color: rgb(255,255,255);")
        self.savename.setObjectName("savename")
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "new_team"))
        self.label.setText(_translate("Dialog", "Create New Team"))
        self.team_name.setPlaceholderText(_translate("Dialog", "enter team name"))
        self.savename.setText(_translate("Dialog", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
