# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'power_main_pi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 500)
        MainWindow.setMinimumSize(QtCore.QSize(750, 500))
        MainWindow.setMaximumSize(QtCore.QSize(750, 500))
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url(:/image/background.jpg);")
        self.centralwidget.setObjectName("centralwidget")
        self.greenStatus = QtWidgets.QLabel(self.centralwidget)
        self.greenStatus.setEnabled(False)
        self.greenStatus.setGeometry(QtCore.QRect(80, 140, 125, 65))
        self.greenStatus.setStyleSheet("background-image: url(:/image/green.jpg);")
        self.greenStatus.setText("")
        self.greenStatus.setObjectName("greenStatus")
        self.redStatus = QtWidgets.QLabel(self.centralwidget)
        self.redStatus.setGeometry(QtCore.QRect(80, 140, 125, 65))
        self.redStatus.setStyleSheet("background-image: url(:/image/red.jpg);")
        self.redStatus.setText("")
        self.redStatus.setObjectName("redStatus")
        self.yellowStatus = QtWidgets.QLabel(self.centralwidget)
        self.yellowStatus.setEnabled(True)
        self.yellowStatus.setGeometry(QtCore.QRect(80, 140, 125, 65))
        self.yellowStatus.setStyleSheet("background-image: url(:/image/yellow.jpg);")
        self.yellowStatus.setText("")
        self.yellowStatus.setObjectName("yellowStatus")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 230, 151, 31))
        self.label.setStyleSheet("font: 28pt \"Lao UI\";\n"
"font-weight: bold;\n"
"color: white;\n"
"background-image: url();")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 280, 151, 21))
        self.label_2.setStyleSheet("font: 10pt \"Lao UI\";\n"
"color: white;\n"
"background-image: url();")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 30, 201, 31))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("font: 14pt \"Lao UI\";\n"
"font-weight: bold;\n"
"color: white;\n"
"background-image: url();")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.enableAutoBoot = QtWidgets.QCheckBox(self.centralwidget)
        self.enableAutoBoot.setGeometry(QtCore.QRect(330, 70, 21, 21))
        self.enableAutoBoot.setStyleSheet("background-image: url();\n"
"selection-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lao UI\";\n"
"color: rgb(255, 255, 255);")
        self.enableAutoBoot.setText("")
        self.enableAutoBoot.setObjectName("enableAutoBoot")
        self.enableEveryday = QtWidgets.QCheckBox(self.centralwidget)
        self.enableEveryday.setEnabled(True)
        self.enableEveryday.setGeometry(QtCore.QRect(330, 110, 21, 21))
        self.enableEveryday.setStyleSheet("background-image: url();\n"
"color: white;\n"
"font: 10pt \"Lao UI\";")
        self.enableEveryday.setText("")
        self.enableEveryday.setObjectName("enableEveryday")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(500, 70, 118, 22))
        self.timeEdit.setStyleSheet("background-image: url();")
        self.timeEdit.setObjectName("timeEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 150, 231, 31))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("font: 14pt \"Lao UI\";\n"
"font-weight: bold;\n"
"color: white;\n"
"background-image: url();")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 190, 91, 21))
        self.label_5.setStyleSheet("font: 10pt \"Lao UI\";\n"
"color: white;\n"
"background-image: url();")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.singleTapFunction = QtWidgets.QComboBox(self.centralwidget)
        self.singleTapFunction.setGeometry(QtCore.QRect(430, 190, 161, 22))
        self.singleTapFunction.setStyleSheet("background-image: url();")
        self.singleTapFunction.setObjectName("singleTapFunction")
        self.singleTapFunction.addItem("")
        self.singleTapFunction.addItem("")
        self.DoubleTapFunction = QtWidgets.QComboBox(self.centralwidget)
        self.DoubleTapFunction.setGeometry(QtCore.QRect(430, 230, 161, 22))
        self.DoubleTapFunction.setStyleSheet("background-image: url();")
        self.DoubleTapFunction.setObjectName("DoubleTapFunction")
        self.DoubleTapFunction.addItem("")
        self.DoubleTapFunction.addItem("")
        self.DoubleTapFunction.addItem("")
        self.DoubleTapFunction.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 230, 91, 21))
        self.label_6.setStyleSheet("font: 10pt \"Lao UI\";\n"
"color: white;\n"
"background-image: url();")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.longTapFunction = QtWidgets.QComboBox(self.centralwidget)
        self.longTapFunction.setGeometry(QtCore.QRect(430, 270, 161, 22))
        self.longTapFunction.setStyleSheet("background-image: url();")
        self.longTapFunction.setEditable(False)
        self.longTapFunction.setObjectName("longTapFunction")
        self.longTapFunction.addItem("")
        self.longTapFunction.addItem("")
        self.longTapFunction.addItem("")
        self.longTapFunction.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(330, 270, 91, 21))
        self.label_7.setStyleSheet("font: 10pt \"Lao UI\";\n"
"color: white;\n"
"background-image: url();")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.editSingleTap = QtWidgets.QPushButton(self.centralwidget)
        self.editSingleTap.setGeometry(QtCore.QRect(600, 190, 61, 23))
        self.editSingleTap.setStyleSheet("background-image: url();")
        self.editSingleTap.setObjectName("editSingleTap")
        self.editDoubleTap = QtWidgets.QPushButton(self.centralwidget)
        self.editDoubleTap.setGeometry(QtCore.QRect(600, 230, 61, 23))
        self.editDoubleTap.setStyleSheet("background-image: url();")
        self.editDoubleTap.setObjectName("editDoubleTap")
        self.editLongTap = QtWidgets.QPushButton(self.centralwidget)
        self.editLongTap.setGeometry(QtCore.QRect(600, 270, 61, 23))
        self.editLongTap.setStyleSheet("background-image: url();")
        self.editLongTap.setObjectName("editLongTap")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(330, 320, 261, 31))
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setStyleSheet("font: 14pt \"Lao UI\";\n"
"font-weight: bold;\n"
"color: white;\n"
"background-image: url();")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.safeShutdownLevel = QtWidgets.QComboBox(self.centralwidget)
        self.safeShutdownLevel.setGeometry(QtCore.QRect(430, 360, 161, 22))
        self.safeShutdownLevel.setStyleSheet("background-image: url();")
        self.safeShutdownLevel.setObjectName("safeShutdownLevel")
        self.safeShutdownLevel.addItem("")
        self.safeShutdownLevel.addItem("")
        self.safeShutdownLevel.addItem("")
        self.safeShutdownLevel.addItem("")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 360, 91, 21))
        self.label_9.setStyleSheet("font: 10pt \"Lao UI\";\n"
"color: white;\n"
"background-image: url();")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.modelLabel = QtWidgets.QLabel(self.centralwidget)
        self.modelLabel.setGeometry(QtCore.QRect(60, 111, 161, 20))
        self.modelLabel.setStyleSheet("font: 10pt \"Lao UI\";\n"
"color: white;\n"
"background-image: url();\n"
"font-weight: bold;")
        self.modelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.modelLabel.setObjectName("modelLabel")
        self.hostMsg = QtWidgets.QLabel(self.centralwidget)
        self.hostMsg.setGeometry(QtCore.QRect(330, 420, 181, 21))
        self.hostMsg.setStyleSheet("font: 10pt \"Lao UI\";\n"
"background-image: url();\n"
"color: rgb(173, 173, 173);")
        self.hostMsg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.hostMsg.setObjectName("hostMsg")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(360, 70, 131, 21))
        self.label_10.setStyleSheet("font: 10pt \"Lao UI\";\n"
"color: white;\n"
"background-image: url();")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(360, 110, 131, 21))
        self.label_12.setStyleSheet("font: 10pt \"Lao UI\";\n"
"color: white;\n"
"background-image: url();")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.yellowStatus.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.enableAutoBoot.raise_()
        self.enableEveryday.raise_()
        self.timeEdit.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.singleTapFunction.raise_()
        self.DoubleTapFunction.raise_()
        self.label_6.raise_()
        self.longTapFunction.raise_()
        self.label_7.raise_()
        self.editSingleTap.raise_()
        self.editDoubleTap.raise_()
        self.editLongTap.raise_()
        self.label_8.raise_()
        self.safeShutdownLevel.raise_()
        self.label_9.raise_()
        self.modelLabel.raise_()
        self.redStatus.raise_()
        self.greenStatus.raise_()
        self.hostMsg.raise_()
        self.label_10.raise_()
        self.label_12.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout_PiSugar_Power_Manager_1_0 = QtWidgets.QAction(MainWindow)
        self.actionAbout_PiSugar_Power_Manager_1_0.setObjectName("actionAbout_PiSugar_Power_Manager_1_0")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout_PiSugar_Power_Manager_v1_0 = QtWidgets.QAction(MainWindow)
        self.actionAbout_PiSugar_Power_Manager_v1_0.setObjectName("actionAbout_PiSugar_Power_Manager_v1_0")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuGithub = QtWidgets.QAction(MainWindow)
        self.menuGithub.setObjectName("menuGithub")
        self.menuClose = QtWidgets.QAction(MainWindow)
        self.menuClose.setObjectName("menuClose")
        self.menuServer_Setting = QtWidgets.QAction(MainWindow)
        self.menuServer_Setting.setObjectName("menuServer_Setting")
        self.menuAbout = QtWidgets.QAction(MainWindow)
        self.menuAbout.setObjectName("menuAbout")
        self.menuEnable_Sever = QtWidgets.QAction(MainWindow)
        self.menuEnable_Sever.setCheckable(True)
        self.menuEnable_Sever.setObjectName("menuEnable_Sever")
        self.menuFile.addAction(self.menuEnable_Sever)
        self.menuFile.addAction(self.menuServer_Setting)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuClose)
        self.menuHelp.addAction(self.menuGithub)
        self.menuHelp.addAction(self.menuAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PiSugar Power Manager"))
        self.label.setText(_translate("MainWindow", "100%"))
        self.label_2.setText(_translate("MainWindow", "Output Votage: 5.28V"))
        self.label_3.setText(_translate("MainWindow", "Auto Boot"))
        self.label_4.setText(_translate("MainWindow", "Button Function"))
        self.label_5.setText(_translate("MainWindow", "Single Tap"))
        self.singleTapFunction.setItemText(0, _translate("MainWindow", "None"))
        self.singleTapFunction.setItemText(1, _translate("MainWindow", "Custom Shell"))
        self.DoubleTapFunction.setItemText(0, _translate("MainWindow", "None"))
        self.DoubleTapFunction.setItemText(1, _translate("MainWindow", "Shutdown"))
        self.DoubleTapFunction.setItemText(2, _translate("MainWindow", "Reboot"))
        self.DoubleTapFunction.setItemText(3, _translate("MainWindow", "Custom Shell"))
        self.label_6.setText(_translate("MainWindow", "Double Taps"))
        self.longTapFunction.setItemText(0, _translate("MainWindow", "None"))
        self.longTapFunction.setItemText(1, _translate("MainWindow", "Shutdown"))
        self.longTapFunction.setItemText(2, _translate("MainWindow", "Reboot"))
        self.longTapFunction.setItemText(3, _translate("MainWindow", "Custom Shell"))
        self.label_7.setText(_translate("MainWindow", "Long Tap"))
        self.editSingleTap.setText(_translate("MainWindow", "Edit"))
        self.editDoubleTap.setText(_translate("MainWindow", "Edit"))
        self.editLongTap.setText(_translate("MainWindow", "Edit"))
        self.label_8.setText(_translate("MainWindow", "Safe Shutdown"))
        self.safeShutdownLevel.setItemText(0, _translate("MainWindow", "<= 5%"))
        self.safeShutdownLevel.setItemText(1, _translate("MainWindow", "<= 3%"))
        self.safeShutdownLevel.setItemText(2, _translate("MainWindow", "<= 1%"))
        self.safeShutdownLevel.setItemText(3, _translate("MainWindow", "Disable"))
        self.label_9.setText(_translate("MainWindow", "Battery Level"))
        self.modelLabel.setText(_translate("MainWindow", "PiSugar 2 Pro"))
        self.hostMsg.setText(_translate("MainWindow", "Host: 192.169.1.92:3010"))
        self.label_10.setText(_translate("MainWindow", "Enable Auto Boot"))
        self.label_12.setText(_translate("MainWindow", "Execute Everyday"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout_PiSugar_Power_Manager_1_0.setText(_translate("MainWindow", "About PiSugar Power Manager 1.0"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout_PiSugar_Power_Manager_v1_0.setText(_translate("MainWindow", "About PiSugar Power Manager v1.0"))
        self.actionClose.setText(_translate("MainWindow", "Close Window"))
        self.menuGithub.setText(_translate("MainWindow", "Visit Github Repository"))
        self.menuClose.setText(_translate("MainWindow", "Close"))
        self.menuServer_Setting.setText(_translate("MainWindow", "Server Setting"))
        self.menuAbout.setText(_translate("MainWindow", "About PiSugar Power Manager v1.0"))
        self.menuEnable_Sever.setText(_translate("MainWindow", "Enable Sever"))

import ui.sugar_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
