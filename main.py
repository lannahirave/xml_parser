# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from strategy import Context

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(785, 585)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(785, 585))
        MainWindow.setMaximumSize(QtCore.QSize(785, 585))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("background-color: rgb(231, 231, 231);")
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 170, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(120, 20, 200, 18))
        self.comboBox_5.setMaximumSize(QtCore.QSize(200, 40))
        self.comboBox_5.setObjectName("comboBox_5")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 110, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 140, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 200, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(20, 20, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 80, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(120, 50, 200, 18))
        self.comboBox_6.setMaximumSize(QtCore.QSize(200, 40))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_8 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_8.setGeometry(QtCore.QRect(120, 80, 200, 18))
        self.comboBox_8.setMaximumSize(QtCore.QSize(200, 40))
        self.comboBox_8.setObjectName("comboBox_8")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 50, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.comboBox_9 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_9.setGeometry(QtCore.QRect(120, 110, 200, 18))
        self.comboBox_9.setMaximumSize(QtCore.QSize(200, 40))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_10 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_10.setGeometry(QtCore.QRect(120, 140, 200, 18))
        self.comboBox_10.setMaximumSize(QtCore.QSize(200, 40))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_11 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_11.setGeometry(QtCore.QRect(120, 170, 200, 18))
        self.comboBox_11.setMaximumSize(QtCore.QSize(200, 40))
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_12 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_12.setGeometry(QtCore.QRect(120, 200, 200, 18))
        self.comboBox_12.setMaximumSize(QtCore.QSize(200, 40))
        self.comboBox_12.setObjectName("comboBox_12")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 370, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 230, 81, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 340, 81, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 310, 82, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 340, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(330, 10, 441, 521))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 310, 81, 23))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 370, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 280, 81, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 785, 21))
        self.menubar.setObjectName("menubar")
        self.menu_0 = QtWidgets.QMenu(self.menubar)
        self.menu_0.setObjectName("menu_0")
        self.menu_1 = QtWidgets.QMenu(self.menubar)
        self.menu_1.setObjectName("menu_1")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.handleOpen)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu_0.addAction(self.actionOpen)
        self.menu_0.addAction(self.actionExit)
        self.menu_1.addAction(self.actionAbout)
        self.menubar.addAction(self.menu_0.menuAction())
        self.menubar.addAction(self.menu_1.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.current_file = ''
        
    
    def handleOpen(self):
        try:
            path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '', 'xml(*.xml)')
            if path[0] != '' and path is not None:
                print(path[0])
                self.current_file = path[0]
        except Exception as exp:
            print(exp)
            return
        f = open(self.current_file, 'r')
        print(f)
        self.textBrowser.setText(f.read())
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XML"))
        self.checkBox_6.setText(_translate("MainWindow", "Умови"))
        self.checkBox_4.setText(_translate("MainWindow", "Версія"))
        self.checkBox_5.setText(_translate("MainWindow", "Автор"))
        self.checkBox_7.setText(_translate("MainWindow", "Реєстріції"))
        self.checkBox_1.setText(_translate("MainWindow", "Назва"))
        self.checkBox_3.setText(_translate("MainWindow", "Тип"))
        self.checkBox_8.setText(_translate("MainWindow", "Зміст"))
        self.pushButton.setText(_translate("MainWindow", "Видалити"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Пошук за параметрами.</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Пошук"))
        self.pushButton_3.setText(_translate("MainWindow", "Зберігти"))
        self.radioButton.setText(_translate("MainWindow", "SAX API"))
        self.radioButton_2.setText(_translate("MainWindow", "DOM API"))
        self.pushButton_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>Трансформує XML в HTML.</p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Трансформація"))
        self.radioButton_3.setText(_translate("MainWindow", "ETree api"))
        self.pushButton_5.setText(_translate("MainWindow", "Відкрити"))
        self.menu_0.setTitle(_translate("MainWindow", "Файл"))
        self.menu_1.setTitle(_translate("MainWindow", "Допомога"))
        self.actionOpen.setText(_translate("MainWindow", "Відкрити"))
        self.action_2.setText(_translate("MainWindow", "Зберігти"))
        self.action_3.setText(_translate("MainWindow", "Зберігти як"))
        self.actionExit.setText(_translate("MainWindow", "Вийти"))
        self.actionAbout.setText(_translate("MainWindow", "Про додаток"))