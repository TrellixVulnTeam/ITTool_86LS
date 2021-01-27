# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_LoadScan.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameLoadScan(object):
    def setupUi(self, FrameLoadScan):
        FrameLoadScan.setObjectName("FrameLoadScan")
        FrameLoadScan.resize(250, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FrameLoadScan.sizePolicy().hasHeightForWidth())
        FrameLoadScan.setSizePolicy(sizePolicy)
        FrameLoadScan.setMinimumSize(QtCore.QSize(250, 500))
        FrameLoadScan.setMaximumSize(QtCore.QSize(2500, 500))
        FrameLoadScan.setLayoutDirection(QtCore.Qt.LeftToRight)
        FrameLoadScan.setFrameShape(QtWidgets.QFrame.Box)
        self.gridLayoutWidget = QtWidgets.QWidget(FrameLoadScan)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 262, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.layoutLoadScan = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.layoutLoadScan.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.layoutLoadScan.setContentsMargins(0, 0, 0, 0)
        self.layoutLoadScan.setObjectName("layoutLoadScan")
        self.btnLoad = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnLoad.setObjectName("btnLoad")
        self.layoutLoadScan.addWidget(self.btnLoad, 5, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(50, 20))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.layoutLoadScan.addWidget(self.label, 1, 1, 1, 1)
        self.dateTimeFrom = QtWidgets.QDateTimeEdit(self.gridLayoutWidget)
        self.dateTimeFrom.setMinimumSize(QtCore.QSize(0, 20))
        self.dateTimeFrom.setMaximumSize(QtCore.QSize(16777215, 30))
        self.dateTimeFrom.setObjectName("dateTimeFrom")
        self.layoutLoadScan.addWidget(self.dateTimeFrom, 2, 1, 1, 1)
        self.dateTimeTo = QtWidgets.QDateTimeEdit(self.gridLayoutWidget)
        self.dateTimeTo.setMaximumSize(QtCore.QSize(16777215, 30))
        self.dateTimeTo.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 2), QtCore.QTime(23, 59, 0)))
        self.dateTimeTo.setObjectName("dateTimeTo")
        self.layoutLoadScan.addWidget(self.dateTimeTo, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setMaximumSize(QtCore.QSize(50, 20))
        self.label_2.setObjectName("label_2")
        self.layoutLoadScan.addWidget(self.label_2, 1, 3, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.gridLayoutWidget)
        self.calendarWidget.setMaximumSize(QtCore.QSize(250, 250))
        self.calendarWidget.setObjectName("calendarWidget")
        self.layoutLoadScan.addWidget(self.calendarWidget, 0, 1, 1, 3, QtCore.Qt.AlignTop)

        self.retranslateUi(FrameLoadScan)
        QtCore.QMetaObject.connectSlotsByName(FrameLoadScan)

    def retranslateUi(self, FrameLoadScan):
        _translate = QtCore.QCoreApplication.translate
        FrameLoadScan.setWindowTitle(_translate("FrameLoadScan", "Frame"))
        self.btnLoad.setText(_translate("FrameLoadScan", "Load"))
        self.label.setText(_translate("FrameLoadScan", "From"))
        self.label_2.setText(_translate("FrameLoadScan", "To"))
