# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1471, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 600))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777214))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:/Picture/Icon/avatar/employee9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layoutMain = QtWidgets.QGridLayout()
        self.layoutMain.setObjectName("layoutMain")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setLineWidth(2)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.layoutMain.addWidget(self.lcdNumber, 0, 1, 1, 1)
        self.toolBoxMenu = QtWidgets.QToolBox(self.centralwidget)
        self.toolBoxMenu.setMinimumSize(QtCore.QSize(200, 500))
        self.toolBoxMenu.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.toolBoxMenu.setFont(font)
        self.toolBoxMenu.setLineWidth(2)
        self.toolBoxMenu.setObjectName("toolBoxMenu")
        self.toolBoxMenuPage1_2 = QtWidgets.QWidget()
        self.toolBoxMenuPage1_2.setGeometry(QtCore.QRect(0, 0, 200, 545))
        self.toolBoxMenuPage1_2.setObjectName("toolBoxMenuPage1_2")
        self.listWidget = QtWidgets.QListWidget(self.toolBoxMenuPage1_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 201, 371))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.toolBoxMenu.addItem(self.toolBoxMenuPage1_2, "")
        self.toolBoxMenuPage1 = QtWidgets.QWidget()
        self.toolBoxMenuPage1.setGeometry(QtCore.QRect(0, 0, 200, 545))
        self.toolBoxMenuPage1.setObjectName("toolBoxMenuPage1")
        self.MenuCard = QtWidgets.QListWidget(self.toolBoxMenuPage1)
        self.MenuCard.setGeometry(QtCore.QRect(0, 0, 200, 371))
        self.MenuCard.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.MenuCard.setFont(font)
        self.MenuCard.setAutoFillBackground(False)
        self.MenuCard.setObjectName("MenuCard")
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("E:/Picture/Icon/Favorites (1)/avatar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.MenuCard.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("E:/Picture/Icon/Favorites (1)/id-card.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.MenuCard.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("E:/Picture/Icon/Favorites (1)/icons8-database-import-500.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.MenuCard.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("E:/Picture/Icon/Favorites (1)/icons8-add-file-500.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.MenuCard.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("E:/Picture/Icon/Favorites (1)/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.MenuCard.addItem(item)
        self.toolBoxMenu.addItem(self.toolBoxMenuPage1, "")
        self.toolBoxMenuPage2 = QtWidgets.QWidget()
        self.toolBoxMenuPage2.setGeometry(QtCore.QRect(0, 0, 200, 545))
        self.toolBoxMenuPage2.setObjectName("toolBoxMenuPage2")
        self.MenuScan = QtWidgets.QListWidget(self.toolBoxMenuPage2)
        self.MenuScan.setGeometry(QtCore.QRect(0, 0, 201, 361))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.MenuScan.setFont(font)
        self.MenuScan.setObjectName("MenuScan")
        item = QtWidgets.QListWidgetItem()
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("E:/Picture/Icon/Favorites (1)/ic_download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon6)
        self.MenuScan.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.MenuScan.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.MenuScan.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.MenuScan.addItem(item)
        self.toolBoxMenu.addItem(self.toolBoxMenuPage2, "")
        self.toolBoxMenuPage3 = QtWidgets.QWidget()
        self.toolBoxMenuPage3.setGeometry(QtCore.QRect(0, 0, 200, 545))
        self.toolBoxMenuPage3.setObjectName("toolBoxMenuPage3")
        self.MenuIT = QtWidgets.QListWidget(self.toolBoxMenuPage3)
        self.MenuIT.setGeometry(QtCore.QRect(0, 0, 201, 331))
        self.MenuIT.setObjectName("MenuIT")
        item = QtWidgets.QListWidgetItem()
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("E:/Picture/Icon/content.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon7)
        self.MenuIT.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("E:/Picture/Icon/exchange.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon8)
        self.MenuIT.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("E:/Picture/Icon/sneakers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon9)
        self.MenuIT.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("E:/Picture/Icon/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon10)
        self.MenuIT.addItem(item)
        self.toolBoxMenu.addItem(self.toolBoxMenuPage3, "")
        self.toolBoxMenuPage4 = QtWidgets.QWidget()
        self.toolBoxMenuPage4.setGeometry(QtCore.QRect(0, 0, 200, 545))
        self.toolBoxMenuPage4.setObjectName("toolBoxMenuPage4")
        self.toolBoxMenu.addItem(self.toolBoxMenuPage4, "")
        self.layoutMain.addWidget(self.toolBoxMenu, 1, 1, 1, 1)
        self.frame = QtWidgets.QWidget(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(250, 500))
        self.frame.setMaximumSize(QtCore.QSize(2000, 1000))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setObjectName("frame")
        self.layoutMain.addWidget(self.frame, 0, 2, 2, 2)
        self.horizontalLayout.addLayout(self.layoutMain)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1471, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TS tool"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "New Item"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.toolBoxMenu.setItemText(self.toolBoxMenu.indexOf(self.toolBoxMenuPage1_2), _translate("MainWindow", "Page"))
        __sortingEnabled = self.MenuCard.isSortingEnabled()
        self.MenuCard.setSortingEnabled(False)
        item = self.MenuCard.item(0)
        item.setText(_translate("MainWindow", "All Staff"))
        item = self.MenuCard.item(1)
        item.setText(_translate("MainWindow", "All Card"))
        item = self.MenuCard.item(2)
        item.setText(_translate("MainWindow", "Import"))
        item = self.MenuCard.item(3)
        item.setText(_translate("MainWindow", "New - Update Card"))
        item = self.MenuCard.item(4)
        item.setText(_translate("MainWindow", "Print"))
        self.MenuCard.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.MenuScan.isSortingEnabled()
        self.MenuScan.setSortingEnabled(False)
        item = self.MenuScan.item(0)
        item.setText(_translate("MainWindow", "Scan Detail"))
        item = self.MenuScan.item(1)
        item.setText(_translate("MainWindow", "Absent"))
        item = self.MenuScan.item(2)
        item.setText(_translate("MainWindow", "Present"))
        item = self.MenuScan.item(3)
        item.setText(_translate("MainWindow", "Card Forgot"))
        self.MenuScan.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.MenuIT.isSortingEnabled()
        self.MenuIT.setSortingEnabled(False)
        item = self.MenuIT.item(0)
        item.setText(_translate("MainWindow", "Inventory software"))
        item = self.MenuIT.item(1)
        item.setText(_translate("MainWindow", "Update Window"))
        item = self.MenuIT.item(2)
        item.setText(_translate("MainWindow", "Update CPA"))
        item = self.MenuIT.item(3)
        item.setText(_translate("MainWindow", "Computer Info"))
        self.MenuIT.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
